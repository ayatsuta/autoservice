from django.urls import path

from workshop.views import (
    index,
    MechanicListView,
    MechanicDetailView,
    MechanicCreateView,
    MechanicUpdateView,
    MechanicDeleteView,
    VehicleListView,
    ClientListView,
    ClientDetailView,
    ManagerListView,
    ManagerDetailView,
    ManagerCreateView,
    VehicleDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("managers/<int:pk>/", ManagerDetailView.as_view(), name="manager-detail"),
    path("managers/create/", ManagerCreateView.as_view(), name="manager-create"),
    path("managers/", ManagerListView.as_view(), name="manager-list"),
    path("mechanics/", MechanicListView.as_view(), name="mechanic-list"),
    path("mechanics/create/", MechanicCreateView.as_view(), name="mechanic-create"),
    path("mechanics/<int:pk>/update/", MechanicUpdateView.as_view(), name="mechanic-update"),
    path("mechanics/<int:pk>/delete/", MechanicDeleteView.as_view(), name="mechanic-delete"),
    path("mechanics/<int:pk>/", MechanicDetailView.as_view(), name="mechanic-detail"),
    path("vehicles/", VehicleListView.as_view(), name="vehicle-list"),
    path("vehicles/<int:pk>/", VehicleDetailView.as_view(), name="vehicle-detail"),
    path("clients/", ClientListView.as_view(), name="client-list"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client-detail"),
]

app_name = "workshop"
