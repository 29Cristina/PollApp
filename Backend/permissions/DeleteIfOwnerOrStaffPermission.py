from rest_framework import permissions


class DeleteIfOwnerOrStaffPermission(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated or request.method == "GET":
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            if request.user.is_superuser or obj.creator == request.user:
                return True
            else:
                return False

        return True