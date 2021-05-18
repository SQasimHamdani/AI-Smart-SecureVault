from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Manager(models.Model):
    user_profile  = models.OneToOneField(User, on_delete=models.CASCADE)
    name    = models.CharField(max_length = 50)
    email   = models.EmailField(unique=True)
    address = models.CharField(max_length = 100)
    phone   = models.CharField(max_length = 15)
    
    # username = models.CharField(max_length = 100, null=True, unique=True)
    # email   = models.EmailField(null=True, default="")
    # password = models.CharField(null=True, max_length = 100)

    def __str__(self):
        return self.name
    
    # def get_loggedin_user(self,request):
    #     user = Manager.objects.all().filter(user = request.user)
    #     return user.name