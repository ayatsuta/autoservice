from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from workshop.models import Manager, Vehicle, Mechanic


class ManagerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Manager
        fields = UserCreationForm.Meta.fields + ("username", "first_name", "last_name")


class VehicleForm(forms.ModelForm):
    mechanics = forms.ModelMultipleChoiceField(
        queryset=Mechanic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Vehicle
        fields = "__all__"


class VehicleSearchForm(forms.Form):
    model = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by model"
            }
        )
    )