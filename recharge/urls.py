"""recharge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from seller.views import SellerInfo
from views import UserInfo, Sidebar

urlpatterns = [
    url(r'^userinfo/', UserInfo.as_view(), name='userinfo'),
    url(r'^sidebar/', Sidebar.as_view(), name='sidebar'),
    url(r'^$', login_required(SellerInfo.as_view()), name='info'),
    url(r'^/', include('runfastauth.urls', namespace='runfastauth')),
    # url(r'^seller/', include('seller.urls', namespace='seller')),

]
