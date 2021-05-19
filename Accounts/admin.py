from django.contrib import admin

from .models import Manager, ManagersLogin
# Register your models here.

admin.site.register(Manager)
admin.site.register(ManagersLogin)