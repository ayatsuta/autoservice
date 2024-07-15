from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
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


class ManagerListView(LoginRequiredMixin, generic.ListView):
    model = Manager


class ManagerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manager
    fields = "__all__"
    success_url = reverse_lazy("workshop:manager-list")


class ManagerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manager


class MechanicListView(LoginRequiredMixin, generic.ListView):
    model = Mechanic
    paginate_by = 10


class MechanicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Mechanic


class VehicleListView(LoginRequiredMixin, generic.ListView):
    model = Vehicle
    paginate_by = 10


class VehicleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Vehicle


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client
    paginate_by = 10


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client

