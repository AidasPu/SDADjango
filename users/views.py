from django.urls import reverse_lazy
from django.shortcuts import HttpResponse, render
from users.models import User
from django.views.generic import CreateView
from .forms import CreateUserForm



def hello(request, word="", word1=""):
    return HttpResponse(f"hello {word} {word1} world!")


def index(request):
    specific_users = User.objects.filter(name__icontains="us")
    context = {"lobbies": specific_users}
    return render(request, "index.html", context=context)


class CreateUser(CreateView):
    model = User
    template_name = "CreateUserForm.html"
    form_class = CreateUserForm
    success_url = reverse_lazy('index')





# sukurti endpointa /lobbies
# islistinti visus lobbies ir userius priklausancius kiekvienam lobby.


# Happy path

# Useris kreipiasi i puslapi ->
# useris siuncia requesta ->
# Laukia ->
# serveris priima ->
# urls.py ->
# iesko pattern(requestas turejo endpointa ir jo ieskos path list) ->
# suranda arba ne ->
# metodas iskviestas ->
# query database ->
# sukuriam context su data ->
# renderina index.html ir perduoda context kintamuosius i template ->
# grazina useriui
