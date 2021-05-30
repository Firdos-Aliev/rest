from rest_framework import permissions


class IsAuth(permissions.BasePermission):
    """Permission to authenticated"""

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False


class IsOwner(permissions.BasePermission):
    """Permission to owners"""

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated and request.user == obj.user:
            return True
        return False