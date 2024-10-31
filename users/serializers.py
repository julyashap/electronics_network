from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    codephrase = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'codephrase',)
