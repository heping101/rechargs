# -*- coding: utf-8 -*-


# Create your views here.
import logging

from django.conf import settings
from django.contrib.auth import login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView

from runfastauth.forms import LoginForm

LOG = logging.getLogger(__name__)



class LoginView(TemplateView):
    template_name = 'runfastauth/login.html'

    def get_context_data(self, **kwargs):
        content = super(LoginView, self).get_context_data()
        form = LoginForm()
        content['form'] = form
        return content

    def post(self, *args, **kwargs):
        content = super(LoginView, self).get_context_data(**kwargs)
        form = LoginForm(self.request, self.request.POST)
        content['form'] = form
        if form.is_valid():
            login(self.request, form.get_user())
            redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
            return HttpResponseRedirect(redirect_to)
        else:
            return self.render_to_response(content)












