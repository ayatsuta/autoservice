from django.urls import path

from workshop.views import (
    index,
    MechanicListView,
    MechanicDetailView,
    MechanicCreateView,
    MechanicUpdateView,
    MechanicDeleteView,
    VehicleListView,
    VehicleDetailView,
    VehicleCreateView,
    VehicleUpdateView,
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    ClientDetailView,
    ManagerListView,
    ManagerDetailView,
    ManagerCreateView,
    ToggleAssignManagerToVehicleView,

)

urlpatterns = [
    path("", index, name="index"),
    path("managers/", ManagerListView.as_view(), name="manager-list"),
    path("managers/<int:pk>/", ManagerDetailView.as_view(), name="manager-detail"),
    path("managers/create/", ManagerCreateView.as_view(), name="manager-create"),
    path("mechanics/", MechanicListView.as_view(), name="mechanic-list"),
    path("mechanics/create/", MechanicCreateView.as_view(), name="mechanic-create"),
    path("mechanics/<int:pk>/update/", MechanicUpdateView.as_view(), name="mechanic-update"),
    path("mechanics/<int:pk>/delete/", MechanicDeleteView.as_view(), name="mechanic-delete"),
    path("mechanics/<int:pk>/", MechanicDetailView.as_view(), name="mechanic-detail"),
    path("vehicles/", VehicleListView.as_view(), name="vehicle-list"),
    path("vehicles/<int:pk>/", VehicleDetailView.as_view(), name="vehicle-detail"),
    path("vehicles/create/", VehicleCreateView.as_view(), name="vehicle-create"),
    path("vehicles/<int:pk>/update/", VehicleUpdateView.as_view(), name="vehicle-update"),
    path(
        'vehicles/<int:pk>/toggle_assign_manager/',
        ToggleAssignManagerToVehicleView.as_view(),
        name='toggle-assign-manager'
    ),
    path("clients/", ClientListView.as_view(), name="client-list"),
    path("clients/create", ClientCreateView.as_view(), name="client-create"),
    path("clients/<int:pk>/update/", ClientUpdateView.as_view(), name="client-update"),
    path("clients/<int:pk>/delete/", ClientDeleteView.as_view(), name="client-delete"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client-detail"),
]

app_name = "workshop"
