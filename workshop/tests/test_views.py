from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from workshop.models import Mechanic, Vehicle, Client

User = get_user_model()


class BaseViewTests(TestCase):
    def setUp(self):
        self.manager_user = User.objects.create_user(
            username="manager1", password="password"
        )
        self.client.login(username="manager1", password="password")
        self.client_instance = Client.objects.create(name="Client1", phone="123456789")
        self.vehicle = Vehicle.objects.create(
            model="TestX", year=2020, VIN="123XYZ", owner=self.client_instance
        )
        self.mechanic = Mechanic.objects.create(name="Mechanic1", speciality="Engine Repair")


class ManagerViewTests(TestCase):
    def setUp(self):
        self.manager_user = User.objects.create_user(
            username="manager1", password="password"
        )
        self.client.force_login(self.manager_user)

    def test_manager_list_view(self):
        response = self.client.get(reverse("workshop:manager-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop/manager_list.html")

    def test_manager_create_view(self):
        response = self.client.get(reverse("workshop:manager-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop/manager_form.html")

    def test_manager_detail_view(self):
        response = self.client.get(reverse("workshop:manager-detail", args=[self.manager_user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop/manager_detail.html")


class MechanicViewTests(BaseViewTests):

    def test_mechanic_list_view(self):
        response = self.client.get(reverse("workshop:mechanic-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop/mechanic_list.html")

    def test_mechanic_create_view(self):
        response = self.client.get(reverse("workshop:mechanic-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop/mechanic_form.html")

    def test_mechanic_detail_view(self):
        response = self.client.get(reverse("workshop:mechanic-detail", args=[self.mechanic.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop/mechanic_detail.html")


class VehicleViewTests(BaseViewTests):

    def test_vehicle_list_view(self):
        response = self.client.get(reverse("workshop:vehicle-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop/vehicle_list.html")

    def test_vehicle_create_view(self):
        response = self.client.get(reverse("workshop:vehicle-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop/vehicle_form.html")

    def test_vehicle_detail_view(self):
        response = self.client.get(reverse("workshop:vehicle-detail", args=[self.vehicle.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop/vehicle_detail.html")


class ToggleAssignManagerToVehicleTests(BaseViewTests):
    def test_toggle_assign_manager_to_vehicle_assign(self):
        response = self.client.post(reverse("workshop:toggle-assign-manager", args=[self.vehicle.pk]))
        self.vehicle.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.vehicle.manager, self.manager_user)

    def test_toggle_assign_manager_to_vehicle_unassign(self):
        self.vehicle.manager = self.manager_user
        self.vehicle.save()
        response = self.client.post(reverse("workshop:toggle-assign-manager", args=[self.vehicle.pk]))
        self.vehicle.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertIsNone(self.vehicle.manager)
