from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from workshop.models import Vehicle, Client, Mechanic


class ManagerModelTests(TestCase):
    def setUp(self):
        self.manager = get_user_model().objects.create_user(
            username="manager1",
            password="password",
            first_name="test",
            last_name="test"
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.manager.get_absolute_url(),
            reverse(
                "workshop:manager-detail",
                args=[str(self.manager.id)]
            )
        )

    def test_manager_str(self):
        self.assertEqual(
            str(self.manager),
            f"{self.manager.username} : {self.manager.first_name} {self.manager.last_name}"
        )


class VehicleModelTests(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name="Client1", phone="123456789")
        self.manager = get_user_model().objects.create_user(username="manager1", password="password")
        self.vehicle = Vehicle.objects.create(
            model="textX",
            year=2010,
            VIN="123ABC",
            owner=self.client,
            manager=self.manager,
        )
        self.mechanic = Mechanic.objects.create(name="Mechanic1", speciality="General Repair")
        self.vehicle.mechanics.add(self.mechanic)

    def test_get_absolute_url(self):
        self.assertEqual(self.vehicle.get_absolute_url(),
                         reverse("workshop:vehicle-detail", args=[str(self.vehicle.id)]))

    def test_vehicle_mechanics(self):
        self.assertIn(self.mechanic, self.vehicle.mechanics.all())

    def test_vehicle_manager(self):
        self.assertEqual(self.vehicle.manager, self.manager)

    def test_vehicle_str(self):
        self.assertEqual(
            str(self.vehicle),
            f"{self.vehicle.model} - {self.vehicle.owner}"
        )


class MechanicModelTests(TestCase):
    def setUp(self):
        self.mechanic = Mechanic.objects.create(name="Mechanic1", speciality="General Repair")

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
