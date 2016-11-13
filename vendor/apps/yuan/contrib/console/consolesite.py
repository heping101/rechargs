# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  验证相关的重载函数.

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.admin.sites import AdminSite
from django.views.decorators.cache import never_cache
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from yuan.contrib.console.forms import AdminEmailAuthenticationForm


class ConsoleSite(AdminSite):
    # def __init__(self, name = None, app_name = 'admin'):
    #     super(ConsoleSite, self).__init__(name, app_name)
    #     self.root_path = '' # 覆盖默认根路径

    @never_cache
    def login(self, request, extra_context=None):
        """
        Displays the admin login form for the given HttpRequest.
        """
        if request.method == 'GET' and self.has_permission(request):
            # Already logged-in, redirect to admin index
            index_path = reverse('admin:index', current_app=self.name)
            return HttpResponseRedirect(index_path)

        # from django.contrib.auth.views import login
        from yuan.contrib.console.views import admin_login as login
        context = dict(self.each_context(request),
            title=_('Administrator Sign In'),
            app_path=request.get_full_path(),
        )
        if (REDIRECT_FIELD_NAME not in request.GET and
                REDIRECT_FIELD_NAME not in request.POST):
            context[REDIRECT_FIELD_NAME] = reverse('admin:index', current_app=self.name)
        context.update(extra_context or {})

        defaults = {
            'extra_context': context,
            'current_app': self.name,
            'authentication_form': self.login_form or AdminEmailAuthenticationForm,
            'template_name': self.login_template or 'admin/login.html',
        }
        request.current_app = self.name
        return login(request, **defaults)

# This global object represents the default admin site, for the common case.
# You can instantiate AdminSite in your own code to create a custom admin site.
site = ConsoleSite()
