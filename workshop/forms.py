from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from workshop.models import Manager


class ManagerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Manager
        fields = UserCreationForm.Meta.fields + ("username", "first_name", "last_name",)
