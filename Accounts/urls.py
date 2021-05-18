from django.urls import path,include
from django.contrib import admin
from Accounts import views
    

urlpatterns = [

    path('', views.home, name = "home"),
    
    path('admin_login', views.admin_login, name = "admin_login"),
    path('admin/logout/', views.admin_signout),

    path('manager_login', views.manager_login, name = "manager_login"),
    path('manager_register', views.manager_register, name = "manager_register"),
    path('manager_signout', views.manager_signout, name = "manager_signout"),

    path('step1', views.step1, name = "step1"),
    path('step2', views.step2, name = "step2"),
    path('step3', views.step3, name = "step3"),
    
    # path('login', views.login, name = "login"),
    # path('register', views.register, name = "register"),
    # path('signout', views.signout, name = "signout"),
]