from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем!"
    def has_permission(self, request, view):

        return request.user == view.get_object().owner


class IsModerator(BasePermission):
    message = "Вы не являетесь модератором!"
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
