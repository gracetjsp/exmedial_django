from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request,"usename already used")
                return redirect("register")
            elif User.objects.filter(email = email).exists():
                messages.info(request,"email already used")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
            return redirect("login")
                
        else:
            messages.info(request,"password miss matched")
            return redirect("register") 

    return render(request,'register.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid credential")
            return redirect("login")
    return render(request,"login.html")
def home(request):
    return render(request,'home.html')
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect("login")