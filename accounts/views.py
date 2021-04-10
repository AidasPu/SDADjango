from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from accounts.forms import CreateUserCustomForm
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from django.utils.translation import gettext as _


@login_required
def hello(request):
    return render(request, "index.html")


def index(request):
    context = {'translate_this': _("a sentence")}

    return render(request, "index.html", context)

def something(request):
    translate_this = _("another sentence")
    return render(request, "home.html", translate_this)


def register(request):
    form = CreateUserCustomForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {"form": form}
    return render(request, 'register.html', context)

# add another field
