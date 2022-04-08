from rest_framework.permissions import BasePermission


class IsUserOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id


class DenyAny(BasePermission):
    def has_permission(self, request, view):
        return False
