# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'login/$', LoginView.as_view, name='login')


    )