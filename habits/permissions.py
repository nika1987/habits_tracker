from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Доступ запрещен'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user or request.user.is_staff:
            return True
        return False
