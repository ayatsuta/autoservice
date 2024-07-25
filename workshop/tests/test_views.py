from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


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

