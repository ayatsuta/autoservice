from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from workshop.forms import ManagerCreationForm, VehicleForm, VehicleSearchForm

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
    form_class = ManagerCreationForm


class ManagerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manager


class MechanicListView(LoginRequiredMixin, generic.ListView):
    model = Mechanic
    paginate_by = 10


class MechanicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Mechanic
    fields = "__all__"
    success_url = reverse_lazy("workshop:mechanic-list")


class MechanicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Mechanic
    fields = "__all__"
    success_url = reverse_lazy("workshop:mechanic-list")


class MechanicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Mechanic
    success_url = reverse_lazy("workshop:mechanic-list")
    template_name = "workshop/mechanic_confirm_delete.html"


class MechanicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Mechanic


class VehicleListView(LoginRequiredMixin, generic.ListView):
    model = Vehicle
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = VehicleSearchForm(
            initial={"model": self.request.GET.get("model", "")}
        )
        return context

    def get_queryset(self):
        queryset = Vehicle.objects.select_related("owner")
        form = VehicleSearchForm(self.request.GET)
        if form.is_valid() and form.cleaned_data["model"]:
            queryset = queryset.filter(model__icontains=form.cleaned_data["model"])
        return queryset


class VehicleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Vehicle
    form_class = VehicleForm


class VehicleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Vehicle
    form_class = VehicleForm


class VehicleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Vehicle


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client
    paginate_by = 10


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Client
    fields = "__all__"
    success_url = reverse_lazy("workshop:client-list")


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Client
    fields = "__all__"
    success_url = reverse_lazy("workshop:client-list")


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Client
    success_url = reverse_lazy("workshop:client-list")
    template_name = "workshop/client_delete.html"


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client

