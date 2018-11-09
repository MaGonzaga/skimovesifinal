from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')

def my_logout(request):
    logout(request)
    return redirect('home')
