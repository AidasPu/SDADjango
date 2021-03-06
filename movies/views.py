from django.shortcuts import render
from django.contrib import sessions
from movies.models import Actor, Movie
from django.views.generic import CreateView, ListView
from movies.forms import MovieForm, ActorForm
from django.contrib.auth.mixins import PermissionRequiredMixin


class Create_actor(CreateView):
    model = Actor
    form_class = ActorForm
    template_name = "create_actor.html"
    success_url = "/actor/list"


class Create_movie(PermissionRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "create_movie.html"
    permission_required = 'movies.add_movie'
    success_url = "/movie/list"


class MovieListView(ListView):
    model = Movie
    template_name = "movie_list.html"


class ActorListView(ListView):
    model = Actor
    template_name = "actor_list.html"
