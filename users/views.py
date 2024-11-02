from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.models import User
from users.permissions import IsCorrectCodePhrase
from users.serializers import UserSerializer, CodePhraseSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Представление для создания объекта модели User"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny & IsCorrectCodePhrase]

    @swagger_auto_schema(
        query_serializer=CodePhraseSerializer()
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Представление для удаления объекта модели User"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny & IsCorrectCodePhrase]

    @swagger_auto_schema(
        query_serializer=CodePhraseSerializer()
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Представление для обновления объекта модели User"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny & IsCorrectCodePhrase]

    @swagger_auto_schema(
        query_serializer=CodePhraseSerializer()
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def perform_update(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для просмотра объекта модели User"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny & IsCorrectCodePhrase]

    @swagger_auto_schema(
        query_serializer=CodePhraseSerializer()
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
