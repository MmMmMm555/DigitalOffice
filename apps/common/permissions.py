from rest_framework.permissions import BasePermission
from apps.users.models import Role


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return view.get_object().imam == request.user


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.SUPER_ADMIN


class IsRegionAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.REGION_ADMIN


class IsDistrictAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.DISTRICT_ADMIN


class IsImam(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.IMAM


class IsDeputy(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.SUB_IMAM
