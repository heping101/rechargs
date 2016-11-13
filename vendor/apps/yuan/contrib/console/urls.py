# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  console相关的url定义

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

# pylint: disable = protected-access

import copy

from django.conf.urls import url, include
from django.contrib import admin

from yuan.contrib import console

#---------------------------------------------------------------------
# 1、利用嫁接实现我们需要的带验证码图片的登录功能
#---------------------------------------------------------------------
admin.autodiscover()
console.site._registry = copy.copy(admin.site._registry)
admin.site = console.site

from . import views

urlpatterns = [
    url(r'^validate.png$', views.dump_authentication_image, name='validate_image'),
    url(r'^javascripts/debug/(?P<file>.+?)/(?P<version>.*?)/$', views.dump_javascript, {'debug': True}, name='dump_debug_javascript'),
    url(r'^javascripts/(?P<file>.+?)/(?P<version>.*?)/$', views.dump_javascript, name='dump_javascript'),
    url(r'', include(admin.site.urls)),
]
