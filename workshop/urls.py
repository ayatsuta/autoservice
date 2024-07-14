from django.urls import path

from workshop.views import index, MechanicListView

urlpatterns = [
    path("", index, name="index"),
    path("Mechanics/", MechanicListView.as_view(), name="Mechanic-list")
]

app_name = "workshop"
