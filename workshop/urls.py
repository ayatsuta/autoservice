from django.urls import path

from workshop.views import index, MechanicListView, VehicleListView, ClientListView, ManagerListView

urlpatterns = [
    path("", index, name="index"),
    path("managers/", ManagerListView.as_view(), name="manager-list"),
    path("mechanics/", MechanicListView.as_view(), name="mechanic-list"),
    path("vehicles/", VehicleListView.as_view(), name="vehicle-list"),
    path("clients/", ClientListView.as_view(), name="client-list"),
]

app_name = "workshop"
