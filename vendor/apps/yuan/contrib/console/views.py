# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  管理端登陆View对象

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

import os

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.conf import settings

from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.contrib.auth.views import deprecate_current_app
from django.contrib.sites.shortcuts import get_current_site

from yuan.http import authentication
from yuan.contrib.console.forms import AdminEmailAuthenticationForm


@deprecate_current_app
@sensitive_post_parameters()
@csrf_protect
@never_cache
def admin_login(request, template_name='admin/login.html',
                redirect_field_name=REDIRECT_FIELD_NAME,
                authentication_form=AdminEmailAuthenticationForm,
                extra_context=None):
    """
    Displays the admin login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():
            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    # 重新生成验证码
    authentication.new_authentication_code(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context)


def dump_authentication_image(request):
    """ 显示验证码图片 """
    return authentication.dump_authentication_code(request)


def dump_javascript(request, js_file, version, debug=False):
    routes = ['javascripts', ]
    if debug:
        routes.append('source')
    routes.append(js_file)
    media_path = os.path.join(*routes)
    return render_to_response(
        media_path,
        context=RequestContext(request),
        content_type='application/javascript')

#if not settings.DEBUG:
#    dump_javascript = page_cache(dump_javascript)
#    dump_javascript = page_cache(dump_javascript, settings.CACHE_MIDDLEWARE_SECONDS)
