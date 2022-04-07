from rest_framework.permissions import BasePermission


class IsUserPostOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id
