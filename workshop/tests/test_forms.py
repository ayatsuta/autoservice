from django.test import TestCase

from workshop.forms import ManagerCreationForm, VehicleForm, VehicleSearchForm
from workshop.models import Manager, Mechanic, Vehicle, Client
from django.contrib.auth import get_user_model


class ManagerCreationFormTest(TestCase):
    def test_form_valid(self):
        form_data = {
            "username": "admin",
            "password1": "Pass123456",
            "password2": "Pass123456",
            "first_name": "test_first",
            "last_name": "test_last",
        }
        form = ManagerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())


class VehicleFormTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name="Client One")
        self.manager = get_user_model().objects.create_user(
            username="manager", password="password123"
        )
        self.mechanic1 = Mechanic.objects.create(name="Mechanic One")
        self.mechanic2 = Mechanic.objects.create(name="Mechanic Two")

    def test_form_valid(self):
        form_data = {
            "model": "Test Model",
            "year": 2000,
            "VIN": "1HGBH41JXMN000000",
            "owner": self.client.id,
            "manager": self.manager.id,
        }
        form = VehicleForm(data=form_data)
        form.fields["mechanics"].queryset = Mechanic.objects.all()
        form.initial["mechanics"] = [self.mechanic1.pk, self.mechanic2.pk]

        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_form_invalid_missing_required_field(self):
        form_data = {
            "model": "Test Model",
            "year": 2000,
            "owner": self.client.id,
            "manager": self.manager.id,
        }
        form = VehicleForm(data=form_data)
        form.fields['mechanics'].queryset = Mechanic.objects.all()

        self.assertFalse(form.is_valid())
