from django.shortcuts import HttpResponse, render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


@login_required
def hello(request, word="", word1=""):
    return HttpResponse(f"hello {word} {word1} world!")


def index(request):
    return render(request, "index.html")
