from django.contrib.auth.models import AbstractUser
from django.db import models


class Manager(AbstractUser):
    class Meta:
        ordering = ("username",)
