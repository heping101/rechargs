# -*- coding:utf-8 -*-

from django import forms
from django.forms.models import ModelForm

from seller.models import Sellers


class SellerEdit(ModelForm):

    class Meta:
        model = Sellers
        fields = ['id', 'username', 'name', 'address', '', '', '', '',]