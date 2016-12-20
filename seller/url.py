# -*- coding: utf-8 -*-
from django.conf.urls import url

from seller.views import SellerInfo

urlpatterns = [
    url(r'sellerinfo/(?P<id>.*)/$', SellerInfo.as_view, name='sellerinfo')

    ]