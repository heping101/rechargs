# -*- coding: utf-8 -*-


# Create your views here.
import logging
from django.shortcuts import render
from django.views.generic.base import TemplateView

LOG = logging.getLogger(__name__)



class LoginView(TemplateView):
    template_name = 'apps/runfastauth/login.html'