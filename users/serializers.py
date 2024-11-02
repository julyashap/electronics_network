from rest_framework import serializers
from users.models import User, CodePhrase


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатора объектов модели User"""

    class Meta:
        model = User
        fields = ('pk', 'email', 'password',)
        read_only_fields = ['pk']


class CodePhraseSerializer(serializers.ModelSerializer):
    """Класс сериализатора объектов модели CodePhrase"""

    class Meta:
        model = CodePhrase
        fields = ('company_name', 'codephrase',)
