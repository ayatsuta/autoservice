from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
