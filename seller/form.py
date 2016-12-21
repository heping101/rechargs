# -*- coding:utf-8 -*-

from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import TextInput

from seller.models import Sellers


class SellerEditForm(ModelForm):

    class Meta:
        model = Sellers
        fields = ['username', 'name', 'address', 'phone_num', 'room_cards', 'seller_type', 'status']
        widgets = {
            'username': TextInput(attrs={'disabled': "disabled"})

        }

