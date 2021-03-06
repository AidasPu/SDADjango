from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from accounts.forms import CreateUserCustomForm
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime


@login_required
def hello(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def register(request):
    form = CreateUserCustomForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            login(request, request.user)
            return redirect('index')
    context = {"form": form}
    return render(request, 'register.html', context)

# Create your views here.
