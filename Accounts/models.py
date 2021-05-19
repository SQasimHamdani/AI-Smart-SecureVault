from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Manager(models.Model):
    user_profile  = models.OneToOneField(User, on_delete=models.CASCADE)
    name    = models.CharField(max_length = 50)
    address = models.CharField(max_length = 300)
    phone   = models.CharField(max_length = 20)
    
    # username = models.CharField(max_length = 100, null=True, unique=True)
    # email   = models.EmailField(null=True, default="")
    # password = models.CharField(null=True, max_length = 100)

    def __str__(self):
        return self.name

class ManagersLogin(models.Model):
    manager  = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    # face_login = models.DateTimeField(auto_now=True)
    logged_in_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.manager.name)+" Logged in at "+str(self.logged_in_at)