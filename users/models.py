from django.contrib.auth.models import AbstractUser
from django.db import models

# Constants
NULLABLE = {'blank': True, 'null': True}


# User

class User(AbstractUser):
    """Пользователь"""
    username = models.CharField(unique=True, max_length=100, verbose_name="Никнейм в ТГ")
    telegram_id = models.IntegerField(verbose_name="Телеграм ID", **NULLABLE)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'
