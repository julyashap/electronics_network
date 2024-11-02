from rest_framework import serializers
from users.models import User, CodePhrase


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'password',)
        read_only_fields = ['pk']


class CodePhraseQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = CodePhrase
        fields = ('company_name', 'codephrase',)
