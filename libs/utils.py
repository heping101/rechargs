# -*- coding: utf-8 -*-

"""
  recharge version 1.0

  常用工具

  @author wangyonghui <wangyonghuimail@163.com>
  @copyright Copyright (c) 2016 runfast.cn
  @link http://runfast.cn
"""
from django.contrib.auth.decorators import login_required
from django.urls.resolvers import RegexURLPattern


def get_vistor_ip(request):
    """
    获取访问用户的IP
    """
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip


def login_filter(urlpatterns, exclude=[]):
    """决定哪些url必须要登陆后才能访问"""
    u = []
    for _url in urlpatterns:
        if _url.name not in exclude:
            s = RegexURLPattern(_url.regex.pattern, login_required(_url.callback), name=_url.name)
            u.append(s)
        else:
            u.append(_url)
    return u
