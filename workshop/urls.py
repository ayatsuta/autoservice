from django.urls import path

from workshop.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "workshop"
