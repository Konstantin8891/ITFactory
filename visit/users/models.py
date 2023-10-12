from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Имя', max_length=255, unique=True)
    phone = models.CharField('Телефон', max_length=255, unique=True)
    password = models.CharField('Пароль', max_length=128)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = "Сотрудники"
