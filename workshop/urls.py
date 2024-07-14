from django.urls import path

from workshop.views import index, MechanicListView, VehicleListView, ClientListView

urlpatterns = [
    path("", index, name="index"),
    path("mechanics/", MechanicListView.as_view(), name="mechanic-list"),
    path("vehicles/", VehicleListView.as_view(), name="vehicle-list"),
    path("clients/", ClientListView.as_view(), name="client-list"),
]

app_name = "workshop"
