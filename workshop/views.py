from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from workshop.models import Manager, Client, Vehicle, Mechanic


def index(request: HttpRequest) -> HttpResponse:
    num_managers = Manager.objects.count()
    num_clients = Client.objects.count()
    num_vehicles = Vehicle.objects.count()
    num_mechanics = Mechanic.objects.count()
    context = {
        "num_managers": num_managers,
        "num_vehicles": num_vehicles,
        "num_clients": num_clients,
        "num_mechanics": num_mechanics,
    }
    return render(request, "workshop/index.html", context=context)


class ManagerListView(generic.ListView):
    model = Manager


class MechanicListView(generic.ListView):
    model = Mechanic
    paginate_by = 10


class VehicleListView(generic.ListView):
    model = Vehicle
    paginate_by = 10


class VehicleDetailView(generic.DetailView):
    model = Vehicle


class ClientListView(generic.ListView):
    model = Client
    paginate_by = 10


class MechanicDetailView(generic.DetailView):
    model = Mechanic
