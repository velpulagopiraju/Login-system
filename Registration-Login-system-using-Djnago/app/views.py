from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def homepage(request):
    return render(request,'home.html')

def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            return HttpResponse('password and conform password is incorrect')
        else:
            myuser = User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('signinpage')

    return render(request,'signup.html')

def signinpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse('username and password are not correct')
    
    return render(request,'signin.html')

def forgotpage(request):
    return render(request,'forgot.html')

def dashboard(request):
    return render(request,'dashboard.html')


