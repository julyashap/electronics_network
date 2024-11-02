from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from users.models import CodePhrase


class IsCorrectCodePhrase(permissions.BasePermission):
    def has_permission(self, request, view):
        company_name = request.data.get('company_name')
        codephrase = request.data.get('codephrase')

        if CodePhrase.objects.filter(company_name=company_name, codephrase=codephrase):
            return True

        raise PermissionDenied(f"Кодовая фраза '{codephrase}' для {company_name} неверна!")
