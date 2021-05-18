from os import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
# Create your views he


from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import logout
from .models import Manager

def get_username(request):
    if request.user.is_authenticated:
        username = Manager.objects.filter(user_profile=request.user.id)[0]
    else:
        username=" "
    
    return username

def home(request):
    username = get_username(request)
    context ={
        "username" : username,
    }
    return render(request, 'Accounts/index.html', context)

def admin_login(request):
    if request.user.is_authenticated:
        
        if request.user.is_staff:
            return HttpResponseRedirect('admin')
        else:
            return render(request, 'Accounts/manager_login.html')
    

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
        return HttpResponseRedirect("admin", context )
    
    return render(request, 'Accounts/admin_login.html', context)

def admin_signout(request):
    logout(request)
    return redirect('admin_login')

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

def manager_register(request):
    
    if request.method == "POST":
        print('this is a POST Request')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


        print(request.POST.get('name'))
        print(request.POST.get('address'))
        print(request.POST.get('phone'))
        print(request.POST.get('username'))
        print(request.POST.get('email'))
        print(request.POST.get('password'))
        print(request.POST.get('works_at_showroom'))

        try:
            user = User.objects.create_user(username = username, password = password, email = email)
            user.name = name
            user.save()
        except:
            print("Error when creating user")
            context = {
                "title" : "register",
                "message" : "Error when creating user",
            }
            return render(request, 'Accounts/manager_register.html', context)
        
        try:
            person = Person(  
                            # username = username, 
                            # password = password, 
                            # email = email,
                            person = user,
                            name = name,
                            address = address,
                            phone = phone,
                            )
            person.save()
        except:
            print("Error when creating Person")
            context = {
                "title" : "register",
                "message" : "Error when creating Person",
            }
            return render(request, 'Accounts/manager_register.html', context)
            

        try:
            customer = Customer(customer = person)
            customer.save()
        except:
            print("Error when creating customer")
            context = {
                "title" : "register",
                "message" : "Error when creating customer",
            }
            return render(request, 'Accounts/manager_register.html', context)
        
        print("Success")
        context = {
            "title" : "register",
            "message" : "Success",
        }
        return render(request, 'Accounts/manager_register.html', context)

    else:
        context = {
            "title" : "register",
        }

        return render(request,'Accounts/manager_register.html', context)

def manager_signout(request):
    logout(request)
    return redirect('manager_login')

def step1(request):
    if not request.user.is_authenticated:
        # print('not logged in')
        return HttpResponseRedirect('manager_login')
    message = "Success - You have Logged In"
    username = get_username(request)
    context = {
        "title" : "Login",
        "message" : message,
        "username" : username,
    }
    return render(request, 'Accounts/step1.html', context)

def step2(request):
    if not request.user.is_authenticated:
        # print('not logged in')
        return HttpResponseRedirect('manager_login')
    message = "Success - You Just Completed Step 2"
    username = get_username(request)
    context = {
        "title" : "Login",
        "message" : message,
        "username" : username,
    }
    return render(request, 'Accounts/step2.html', context)
    
def step3(request):
    if not request.user.is_authenticated:
        # print('not logged in')
        return HttpResponseRedirect('manager_login')
    message = "Success - Second Step Completed too"
    username = get_username(request)
    context = {
        "title" : "Login",
        "message" : message,
        "username" : username,
    }
    return render(request, 'Accounts/step3.html', context)