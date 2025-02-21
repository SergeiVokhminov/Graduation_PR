from rest_framework.permissions import BasePermission


class IsCreated(BasePermission):
    """Проверка на создателя объекта."""

    def has_object_permission(self, request, view, obj):
        return obj.habit_creator == request.user


class IsStaff(BasePermission):
    """Проверка, что пользователь является сотрудником"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()


class IsOwner(BasePermission):
    """Проверка, что пользователь является владельцем"""

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
