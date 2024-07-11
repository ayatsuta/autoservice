from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from workshop.models import Vehicle, Client, Mechanic, Manager

admin.site.register(Vehicle)
admin.site.register(Client)
admin.site.register(Mechanic)
admin.site.register(Manager, UserAdmin)
