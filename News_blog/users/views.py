from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .forms import SignUpForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.

def logIn(request:HttpRequest):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('posts_home')
    context = {'form':form}
    return render(request,'users\login.html',context)


def sign_up(request:HttpRequest):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User created succesfully")
            return redirect('login')
    context = {'form':form}
    return render(request,'users\sign_up.html',context) 
    '''
    form = SignUpForm()
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if password == confirm:
            user = User.objects.create_user(username=username,email=email)
            user.set_password(password)
            user.save()
            return redirect('posts_home')
    context = {'form':form}
    return render(request,'users\sign_up.html',context)
    '''
def log_out(request:HttpRequest):
    logout(request)
    return redirect('posts_home')