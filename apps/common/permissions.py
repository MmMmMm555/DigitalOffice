from rest_framework.permissions import BasePermission



class IsOwnerRead(BasePermission):
    def has_permission(self, request, view, obj):
        return request.user.id == obj.imam.id


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == '1'


class IsRegionAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == '2'


class IsDistrictAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == '3'


class IsImam(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == '4'


class IsDeputy(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == '5'