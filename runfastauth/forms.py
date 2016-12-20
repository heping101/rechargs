# -*- coding:utf-8 -*-

from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label=u'用户名', required=True,
                               error_messages={"required": u"请输入用户名"}, )

    password = forms.CharField(widget=forms.PasswordInput, required=True,
                               error_messages={"required": u"请输入密码"})

    error_messages = {
        'invalid_login': "请输入正确的用户名和密码",

    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login')

        return self.cleaned_data

    def get_user(self):

        return self.user
