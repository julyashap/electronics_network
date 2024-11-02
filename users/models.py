from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс модели пользователя в системе"""

    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class CodePhrase(models.Model):
    """Класс модели кодовых фраз для проверки прав доступа в системе"""

    company_name = models.CharField(max_length=100, verbose_name='название компании')
    codephrase = models.CharField(max_length=10, verbose_name='кодовая фраза')

    def __str__(self):
        return f"codephrase {self.codephrase} for {self.company_name}"

    class Meta:
        verbose_name = 'кодовая фраза'
        verbose_name_plural = 'кодовые фразы'
