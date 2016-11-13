# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  http, url 相关的工具函数

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

import json

from django.core.urlresolvers import reverse
from django.http import QueryDict, HttpResponse


def url_join(*args):
    """
    将给定参数拼凑为url地址
    """
    url_sep = u'/'
    url_ret = u''
    if not args:
        return url_ret
    for arg in args:
        if url_ret.endswith(url_sep):
            url_ret = url_ret[:-1]
        if url_ret:
            if arg.startswith(url_sep):
                arg = arg[1:]
            url_ret = url_sep.join((url_ret, arg))
        else:
            url_ret = arg

    return url_ret


def get_request_value(req, name, default=None):
    ret = default
    try:
        ret = req.REQUEST[name]
    except (KeyError, ValueError, TypeError):
        ret = default
    return ret


def reverse_wqs(viewname, urlconf=None, args=None, kwargs=None, prefix=None, rqs='', params=None):
    """
    封装reverse，将query_string以及用户指定的参数也附加到url结尾 (wqs = with_query_string)
    """
    if not isinstance(params, dict):
        params = {}
    uri = reverse(viewname, urlconf, args, kwargs, prefix)
    query_dict = QueryDict(rqs).copy()
    query_dict.update(params)
    if len(query_dict.items()) > 0:
        if uri.find('?') == -1:
            return '%s?%s' % (uri, query_dict.urlencode())
        else:
            return '%s&%s' % (uri, query_dict.urlencode())
    else:
        return uri


class JsonResponse(HttpResponse):
    """
    An HTTP response class that consumes data to be serialized to JSON.

    :param data: Data to be dumped into json. By default only ``dict`` objects
      are allowed to be passed due to a security flaw before EcmaScript 5. See
      the ``safe`` parameter for more information.
    :param safe: Controls if only ``dict`` objects may be serialized. Defaults
      to ``True``.
    """

    def __init__(self, data, safe=False, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError('In order to allow non-dict objects to be '
                            'serialized set the safe parameter to False')
        kwargs.setdefault('content_type', 'application/json; charset=utf-8')
        data = json.dumps(data, ensure_ascii=False)
        super(JsonResponse, self).__init__(content=data, **kwargs)
