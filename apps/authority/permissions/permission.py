# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.permissions import BasePermission

__all__ = [
    "PermissionAPIRequiredMixin", "PermissionAPIListRequiredMixin", "PermissionPageListRequiredMixin"
]


class PermissionAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list = list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class PermissionAPIListRequiredMixin(PermissionAPIRequiredMixin):
    permission_required = u'authority.deveops_api_list_permission'


class PermissionPageListRequiredMixin(PermissionAPIRequiredMixin):
    permission_required = u'authority.deveops_api_list_permission'