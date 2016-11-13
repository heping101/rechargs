# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  Template tags for stml urlize

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

import logging

from django.template import Library, Node, TemplateSyntaxError
from django.core.urlresolvers import NoReverseMatch, reverse
from django.utils.encoding import smart_str
from django.conf import settings

from yuan import get_version
from yuan.http import url_join, reverse_wqs

ASSET_DEFAULT_LANGUAGE = getattr(settings, 'ASSET_DEFAULT_LANGUAGE', 'en')

register = Library()


def resolve_url_for_dynamic_media(path, media_file, mull=None, mode=None):
    """
    根据是否debug模式，返回不同的资源文件的url，比如JS文件的调试与产品版本是不同的

    参数：
    path - 路径参数，比如javascript，stylesheet等
    media_file - 要请求的文件名称
    mull - 是否使用多语言
    mode - 强制使用指定模式，True表示调试模式

    在模板中的使用方法：
    {% load surlize %}
    {% url_for_javascript "yuan.js" %}
    {% url_for_stylesheet "yuan.css" %}
    {% url_for_image "login.png" request.LANGUAGE_CODE %}
    {% url_for_javascript "yuan.js" request.LANGUAGE_CODE %}
    """
    if mode is None:
        mode = settings.DEBUG
    if mull:
        # 多语言版本需要动态加载这些media文件
        version = mull + ':' + getattr(settings, 'SITE_APP_VERSION', get_version())
        if mode:  # 非产品环境或者处于调试模式
            media_url = reverse('dump_debug_javascript', args=[media_file, version])
        else:
            media_url = reverse('dump_javascript', args=[media_file, version])
        logging.debug('Resolved dynamic media url: (%s, %s, %s, %s) => %s', path, media_file, mull, mode, media_url)
    else:
        # 对于英文版本，直接使用静态文件
        prefix = settings.STATIC_URL
        routes = [prefix, path]
        if mode:  # 非产品环境或者处于调试模式
            routes.append('source')
        routes.append(media_file)
        media_url = url_join(*routes)
        logging.debug('Resolved dynamic media url: (%s, %s, %s, %s, %s) => %s', prefix, path, media_file, mull, mode, media_url)
    return media_url


@register.simple_tag
def url_for_dynamic_media(path, media_file, mull=None, mode=None):
    return resolve_url_for_dynamic_media(path, media_file, mull, mode)


@register.simple_tag
def url_for_javascript(js_file, mull=None, mode=None):
    return resolve_url_for_dynamic_media(u'javascripts', js_file, mull, mode)


@register.simple_tag
def url_for_stylesheet(css_file, mull=None):
    """
    css文件，需要处理多语言问题

    参数：
    css_file - 要请求的文件名称
    mull - 是否使用多语言

    在模板中的使用方法：
    {% url_for_stylesheet "yuan.css" %}
    {% url_for_stylesheet "yuan.css" request.LANGUAGE_CODE %}
    """
    path = 'stylesheets'  # 强制为stylesheets
    prefix = settings.STATIC_URL
    routes = [prefix, path]
    # 这里需要语言支持性检查
    if mull:
        if mull not in settings.SUPPORTED_LANGUAGES:
            mull = ASSET_DEFAULT_LANGUAGE  # 让其使用默认语言
        routes.append(u'locale')
        routes.append(mull)
    routes.append(css_file)
    media_url = url_join(*routes)
    logging.debug('Resolved dynamic media url: (%s, %s, %s, %s) => %s', prefix, path, css_file, mull, media_url)
    return media_url


@register.simple_tag
def url_for_image(img_file, mull=None):
    """
    图片只需要处理多语言问题，所以强制关闭调试模式检查

    参数：
    img_file - 要请求的文件名称
    mull - 是否使用多语言

    在模板中的使用方法：
    {% url_for_image "login.png" request.LANGUAGE_CODE %}
    """
    path = 'images'  # 强制为images
    prefix = settings.STATIC_URL
    routes = [prefix, path]
    # 这里需要语言支持性检查
    if mull not in settings.SUPPORTED_LANGUAGES:
        mull = ASSET_DEFAULT_LANGUAGE  # 让其使用默认文件
    routes.append(u'locale')
    routes.append(mull)
    routes.append(img_file)
    media_url = url_join(*routes)
    logging.debug('Resolved dynamic media url: (%s, %s, %s, %s) => %s', prefix, path, img_file, mull, media_url)
    return media_url


class URLNodeWithQS(Node):
    def __init__(self, view_name, args, kwargs, asvar, params):
        self.view_name = view_name
        self.args = args
        self.kwargs = kwargs
        self.asvar = asvar
        self.params = params

    def render(self, context):
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict([(smart_str(k, 'ascii'), v.resolve(context))
                       for k, v in self.kwargs.items()])

        # Try to look up the URL twice: once given the view name, and again
        # relative to what we guess is the "main" app. If they both fail,
        # re-raise the NoReverseMatch unless we're using the
        # {% url ... as var %} construct in which cause return nothing.
        qs = ''
        try:
            request = context['request']
            qs = request.META['QUERY_STRING']
        except (KeyError, AttributeError):
            qs = ''

        url = ''
        try:
            url = reverse_wqs(self.view_name, args=args, kwargs=kwargs, rqs=qs, params=self.params)
        except NoReverseMatch:
            project_name = settings.SETTINGS_MODULE.split('.')[0]
            try:
                url = reverse_wqs(project_name + '.' + self.view_name,
                                  args=args, kwargs=kwargs, rqs=qs, params=self.params)
            except NoReverseMatch:
                if self.asvar is None:
                    raise

        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            return url


@register.tag
def url_wqs(parser, token):
    """
    Returns an absolute URL matching given view with its parameters.

    This is a way to define links that aren't tied to a particular URL
    configuration::

        {% url path.to.some_view arg1,arg2,name1=value1 %}

    The first argument is a path to a view. It can be an absolute python path
    or just ``app_name.view_name`` without the project name if the view is
    located inside the project.  Other arguments are comma-separated values
    that will be filled in place of positional and keyword arguments in the
    URL. All arguments for the URL should be present.

    For example if you have a view ``app_name.client`` taking client's id and
    the corresponding line in a URLconf looks like this::

        (r'^client/(\\d+)/$', 'app_name.client')

    and this app's URLconf is included into the project's URLconf under some
    path::

        (r'^clients/', include('project_name.app_name.urls'))

    then in a template you can create a link for a certain client like this::

        {% url app_name.client client.id %}

    The URL will look like ``/clients/client/123/``.
    """
    bits = token.contents.split(' ')
    if len(bits) < 2:
        raise TemplateSyntaxError("'%s' takes at least one argument"
                                  " (path to a view)" % bits[0])
    viewname = bits[1]
    args = []
    kwargs = {}
    params = {}
    asvar = None

    if len(bits) > 2:
        bits = iter(bits[2:])
        for bit in bits:
            if bit == 'as':
                asvar = bits.next()
                break
            else:
                for arg in bit.split(","):
                    if '=' in arg:
                        key, value = arg.split('=', 1)
                        key = key.strip()
                        kwargs[key] = parser.compile_filter(value)
                    elif ':' in arg:
                        key, value = arg.split(':', 1)
                        key = key.strip()
                        params[key] = parser.compile_filter(value)
                    elif arg:
                        args.append(parser.compile_filter(arg))
    return URLNodeWithQS(viewname, args, kwargs, asvar, params)


class LoadQueryString(Node):
    """
    输出query_string
    """
    def render(self, context):
        try:
            getvars = context['request'].GET.copy()
            if len(getvars.keys()) > 0:
                return "?%s" % getvars.urlencode()
            else:
                return ''
        except (KeyError, AttributeError):
            return ''


@register.tag
def load_query_string(parser, token):
    """
    A templatetag to show the unread-count for a logged in user.
    Store the number of unread messages in the user's inbox to context.
    Usage::
        {% load config %}
        {% load_query_string %}
    """
    return LoadQueryString()
