from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from users.models import CodePhrase
from users.serializers import CodePhraseSerializer


class IsCorrectCodePhrase(permissions.BasePermission):
    """Класс проверки прав доступа пользователя путем проверки введенной им кодовой фразы"""

    def has_permission(self, request, view):
        data = {
            'company_name': request.query_params.get('company_name'),
            'codephrase': request.query_params.get('codephrase')
        }

        serializer = CodePhraseSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        company_name = serializer.validated_data['company_name']
        codephrase = serializer.validated_data['codephrase']

        if CodePhrase.objects.filter(company_name=company_name, codephrase=codephrase):
            return True

        raise PermissionDenied(f"Кодовая фраза '{codephrase}' для {company_name} неверна!")
