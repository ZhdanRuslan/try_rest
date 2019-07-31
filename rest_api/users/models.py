from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    password = models.CharField(max_length=25)
    is_staff = models.BooleanField(default=False, verbose_name='staff account')
    is_active = models.BooleanField(default=False, verbose_name='active account')

    def __str__(self):
        return self.email
