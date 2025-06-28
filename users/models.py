from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    forename = models.CharField(max_length=50, blank=True, verbose_name="Имя")
    information = models.TextField(max_length=200, verbose_name="Описание", blank=True)
    image = models.ImageField(upload_to='image/', verbose_name="Фото", blank=True)

    USERNAME_FIELD = "forename"
    REQUIRED_FIELDS = []

    class Meta():
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.forename