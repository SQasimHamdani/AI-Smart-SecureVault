from os import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import logout
from .models import Manager, ManagersLogin

def get_username(request):
    if request.user.is_authenticated:
        username = User.objects.filter(id=request.user.id)[0]
    else:
        username=" "
    
    return username

def home(request):
    # username = get_username(request)
    # context ={
    #     "username" : username,
    # }
    # return render(request, 'Accounts/index.html', context)
    return render(request, 'Accounts/index.html')

def admin_login(request):
    if request.user.is_authenticated:
        
        if request.user.is_staff:
            return HttpResponseRedirect('admin_home')
        else:
            return HttpResponseRedirect('step1')
    

    if request.method == "POST":
        print('this is a POST Request')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        res = User.objects.filter(username=user)
        try:
            res = res[0].is_staff
            if res:
                print("Request user is Staff")
                auth.login(request, user)
                message = "Success"
            else:
                print("not a staff")
                message = "Error - User is not Admin"
        except:
            print("Credentials not Valid")
            message = "Error - Credentials not Valid"
    else:
        message = ""
    username = get_username(request)
    context = {
        "title" : "Login",
        "message" : message,
        "username" : username,
    }
    if message=="Success":
        return HttpResponseRedirect("admin_home", context )
    
    return render(request, 'Accounts/admin_login.html', context)

def admin_signout(request):
    logout(request)
    return redirect('admin_login')

def admin_home(request):
    managers = Manager.objects.all()
    message = " "
    context = {
        "message" : message,
        "managers" : managers,
        # "username" : username,
    }
    return render(request, 'Accounts/admin_home.html', context)

def admin_managers_login_view(request):
    managers = ManagersLogin.objects.all()
    message = " "
    context = {
        "message" : message,
        "managers" : managers,
        # "username" : username,
    }
    return render(request, 'Accounts/admin_managers_login_view.html', context)

"""
def manager_login(request):
    if request.user.is_authenticated:
        # print('already logged in')
        return HttpResponseRedirect('step1')
    # else:
        # print("Not logged in")
        

    if request.method == "POST":
        print('this is a POST Request')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        res = User.objects.filter(username=user)
        try:
            res = res[0]
            if res:
                print("Request user logged in")
                auth.login(request, user)
                message = "Success"
            else:
                print("not a staff")
                message = "Error - User not found"
        except:
            print("Credentials not Valid")
            message = "Error - Credentials not Valid"
    else:
        message = ""
    username = get_username(request)
    context = {
        "title" : "Login",
        "message" : message,
        "username" : username,
    }
    if message=="Success":
        return HttpResponseRedirect("step1", context )
    
    return render(request, 'Accounts/manager_login.html', context)
"""

"""
def manager_register(request):
    if request.user.is_authenticated:
        # print('already logged in')
        return HttpResponseRedirect('step1')
    message=" "
    if request.method == "POST":
        print('this is a POST Request')

        username = request.POST.get('Username')
        password = request.POST.get('Password')
        email = request.POST.get('Email')

        name = request.POST.get('Name')
        address = request.POST.get('Address')
        phone = request.POST.get('Phone')


        print(request.POST.get('Username'))
        print(request.POST.get('Password'))
        print(request.POST.get('Email'))

        print(request.POST.get('Name'))
        print(request.POST.get('Address'))
        print(request.POST.get('Phone'))
        
        try:
            user = User.objects.create_user(username = username, password = password, email = email)
            user.name = name
            user.save()
            print("Success user")
            message = "Success - user"
            created_user = user
        except:
            print("Error when creating User")
            message = "Error when creating User"
        created_user = User.objects.filter(username = username)[0]
        # print(created_user)
        try:
            Managerr = Manager(
                            user_profile = created_user,
                            name = name,
                            address = address,
                            phone = phone
                            )
            # print(Managerr,"managerr")

            Managerr.save()
            print("Success Manager")
            message = "Success - Manager Account Created"
            user = authenticate(request, username=username, password=password)
            auth.login(request, user)
        except:
            print("Error when creating Manager")
            message =  "Error when creating Manager"

    context = {
        "title" : "register",
        "message" : message,
    }

    return render(request,'Accounts/manager_register.html', context)
"""

"""
def manager_signout(request):
    logout(request)
    return redirect('manager_login')
"""

def step1(request):
    # if not request.user.is_authenticated:
        # print('not logged in')
        # return HttpResponseRedirect('manager_login')
    message = "Success - You have Reached to the first step"
    # username = get_username(request)
    
    context = {
        "title" : "Login",
        "message" : message,
        # "username" : username,
    }
    return render(request, 'Accounts/step1.html', context)

def step2(request):
    # if not request.user.is_authenticated:
        # print('not logged in')
        # return HttpResponseRedirect('manager_login')
    message = "Success - You Just Completed Step 1"
    # username = get_username(request)
    context = {
        "title" : "Login",
        "message" : message,
        # "username" : username,
    }
    return render(request, 'Accounts/step2.html', context)
    
def step3(request):
    # if not request.user.is_authenticated:
        # print('not logged in')
        # return HttpResponseRedirect('manager_login')
    
    if request.method == "POST":
        print('this is a POST Request')
    else:
        message = "Success - Second Step Completed too"
    context = {
        "title" : "Login",
        "message" : message,
        # "username" : username,
    }
    return render(request, 'Accounts/step3.html', context)