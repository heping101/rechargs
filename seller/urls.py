# -*- coding: utf-8 -*-
from django.conf.urls import url

from libs.utils import login_filter
from seller.views import SellerInfo

urlpatterns = [
    # url(r'info/(?P<id>.*)/$', SellerInfo.as_view, name='info')



    ]

urlpatterns = login_filter(urlpatterns)