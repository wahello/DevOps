# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 09 13:50
# Author Yo
# Email YoLoveLife@outlook.com
"""devEops URL Configuration

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
from django.conf.urls import url,include
from .views import IndexView,ErrorView
urlpatterns = [
    # VIEW
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^404/',ErrorView.as_view(),name='404'),
    url(r'^login/', include('validate.urls', namespace='validate')),
    url(r'^manager/', include('manager.urls.views_urls', namespace='manager')),

    # API
    url(r'^api-manager/', include('manager.urls.api_urls', namespace='api-manager')),
]
'''
   
'''
