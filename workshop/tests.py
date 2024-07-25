from django.contrib.auth import get_user_model
from django.test import TestCase

from workshop.models import Vehicle, Client, Mechanic


class ManagerModelTests(TestCase):
    def test_manager_str(self):
        manager = get_user_model().objects.create(
            username="test",
            password="test1234",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(manager),
            f"{manager.username} : {manager.first_name} {manager.last_name}"
        )


class VehicleModelTests(TestCase):
    def test_vehicle_str(self):
        owner = Client.objects.create(name="test_client")
        vehicle = Vehicle.objects.create(
            model="test_vehicle",
            year="2000",
            owner=owner
        )
        self.assertEqual(
            str(vehicle),
            f"{vehicle.model} - {vehicle.owner}"
        )


class MechanicModelTests(TestCase):
    def test_mechanic_str(self):
        mechanic = Mechanic.objects.create(
            name="test_mechanic",
            speciality="test_speciality"
        )
        self.assertEqual(
            str(mechanic),
            f"{mechanic.name} - {mechanic.speciality}"
        )


class ClientModelTests(TestCase):
    def test_client_str(self):
        client = Client.objects.create(
            name="test_client",
            company="test_company",
            phone="test_phone"
        )
        self.assertEqual(
            str(client),
            f"{client.name} - {client.phone}"
        )
