from rest_framework.permissions import BasePermission



class IsOwnerRead(BasePermission):
    def has_permission(self, request, view, obj):
        return request.user.id == obj.imam.id


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'SUPER_ADMIN'


class IsRegionAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'REGION_ADMIN'


class IsDistrictAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'DISTRICT_ADMIN'


class IsImam(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'IMAM'


class IsDeputy(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'DEPUTY'