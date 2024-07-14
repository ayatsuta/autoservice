from django.urls import path

from workshop.views import index, MechanicListView, VehicleListView

urlpatterns = [
    path("", index, name="index"),
    path("mechanics/", MechanicListView.as_view(), name="mechanic-list"),
    path("vehicles/", VehicleListView.as_view(), name="vehicle-list"),
]

app_name = "workshop"
