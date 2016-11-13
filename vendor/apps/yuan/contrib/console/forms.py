# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  管理端登陆Form对象

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy, ugettext as _
from django.conf import settings

User = settings.AUTH_USER_MODEL

ERROR_MESSAGE = ugettext_lazy("Please enter a correct email and password. "
                              "Note that both fields are case-sensitive.")

from yuan.http import authentication


class AdminEmailAuthenticationForm(forms.Form):
    """
    A custom authentication form used in the admin app. Accepts email/password logins.
    """
    email = forms.CharField(label=_("Email Address:"), max_length=100)
    password = forms.CharField(label=_("Your Password:"), widget=forms.PasswordInput)
    authcode = forms.CharField(label=_("Authentication Code:"), max_length=10)
    this_is_the_login_form = forms.BooleanField(widget=forms.HiddenInput, initial=1,
                                                error_messages={'required': ugettext_lazy(
                                                    "Please log in again, because your session has expired.")})

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super(AdminEmailAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        authcode = self.cleaned_data.get('authcode')
        message = ERROR_MESSAGE
        # print email, password, authcode

        # 检查验证码
        if (not authcode) or (not authentication.check_authentication_code(self.request, authcode)):
            raise forms.ValidationError('Authentication code is error.')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                if u'@' not in email:
                    # Mistakenly entered username instead of e-mail address? Look it up.
                    kwargs = {"typo_check": True}
                    maybe_user = authenticate(email=email, password=password, **kwargs)
                    if maybe_user:
                        message = _("Your should use your e-mail address."
                                    " Try '%s' instead.") % maybe_user.email
                raise forms.ValidationError(message)
            elif not self.user_cache.is_active or not self.user_cache.is_staff:
                raise forms.ValidationError(message)
        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
