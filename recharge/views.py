#!/usr/bin/python
# coding:utf-8
from django.views.generic.base import TemplateView



class UserInfo(TemplateView):
    template_name = 'base.html'

class Sidebar(TemplateView):
    template_name = 'menu.html'

