from rest_framework import permissions
from config import settings


class IsCorrectCodephrase(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.data.get('codephrase') in settings.CODEPHRASES
