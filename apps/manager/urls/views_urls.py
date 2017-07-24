# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 10 15:38
# Author Yo
# Email YoLoveLife@outlook.com
from django.conf.urls import url
from rest_framework import viewsets
from .. import views

urlpatterns = [
    url(r'^group$', views.ManagerGroupListView.as_view(), name='group'),
    url(r'^host$', views.ManagerHostListView.as_view(), name='host'),
    url(r'^search$',views.ManagerSearchListView.as_view(),name='search'),
]