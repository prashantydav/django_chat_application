from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout



# Create your views here.

def signup_view(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username = username , password = password1)
        
        if password1 == password2 :
            if User.objects.filter(username = username).exists():
                print("username taken")
                redirect('signup/')
            else:
                user.save()
                print(f"User created named {username}")

        else:
            print("password not matched")
            redirect('signup/')
        return redirect('../login/')

    else:
        return render(request , 'register/signup.html', {})

def login_view(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password = request.POST['password']

        user =authenticate( username = username1 , password = password)

        if user is not None:
            login(request, user)
            return redirect('../../chat/')
    else:

         return render(request , 'register/login.html')