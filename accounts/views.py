from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from .form import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


@login_required(login_url='login')
def registerPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context ={'form':form}
    return render(request, 'register.html',context)


def loginPage(request):    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')


    context ={}
    return render(request,'login.html')
    

def logoutUser(request):
    logout(request)
    return redirect('/login')