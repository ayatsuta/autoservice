from django.contrib.auth.models import AbstractUser
from django.db import models

from autoservice import settings


class Manager(AbstractUser):
    class Meta:
        ordering = ("username",)


class Vehicle(models.Model):
    model = models.CharField(max_length=63)
    year = models.IntegerField()
    VIN = models.CharField(max_length=63, unique=True)
    owner = models.ForeignKey(
        "Client",
        on_delete=models.DO_NOTHING,
        related_name="vehicles"
    )
    mechanics = models.ManyToManyField(
        "Mechanic",
        related_name="vehicles"
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="managed_vehicles"
    )

    def __str__(self):
        return f"{self.model} - {self.owner}"


class Mechanic(models.Model):
    name = models.CharField(max_length=63)
    speciality = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name} - {self.speciality}"


class Client(models.Model):
    name = models.CharField(max_length=63)
    company = models.CharField(max_length=63, null=True, blank=True)
    phone = models.CharField(max_length=63, null=True, blank=True)
