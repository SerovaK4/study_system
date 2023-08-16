from rest_framework.generics import GenericAPIView
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем!"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsModerator(BasePermission):
    message = "Вы не являетесь модератором!"

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
