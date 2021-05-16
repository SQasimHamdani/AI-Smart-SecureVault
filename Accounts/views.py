from os import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
# Create your views he


from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import logout

def home(request):
    return render(request, 'Accounts/index.html')

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
    context = {
        "title" : "Login",
        "message" : message,
    }
    if message=="Success":
        return HttpResponseRedirect("admin", context )
    
    return render(request, 'Accounts/admin_login.html', context)

def admin_signout(request):
    logout(request)
    return redirect('admin_login')

def manager_login(request):
    return render(request, 'Accounts/manager_login.html')

def step1(request):

    return render(request, 'Accounts/step1.html')

def step2(request):
    return render(request, 'Accounts/step2.html')
    
def step3(request):
    return render(request, 'Accounts/step3.html')