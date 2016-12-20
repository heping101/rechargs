from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from seller.models import Sellers


class SellerInfo(TemplateView):
    template_name = 'seller/info.html'

    def get_context_data(self, **kwargs):
        content = super(SellerInfo, self).get_context_data(**kwargs)
        content['object'] = self.request.user
        return content

