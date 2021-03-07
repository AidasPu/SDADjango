from django.urls import path

from movies.views import Create_movie, Create_actor, MovieListView, ActorListView

app_name = 'movies'

urlpatterns = [
    path('movie/create', Create_movie.as_view(), name="create_movie"),
    path('actor/create', Create_actor.as_view(), name="create_actor"),
    path('movie/list', MovieListView.as_view(), name="movie_list"),
    path('actor/list', ActorListView.as_view(), name="actor_list"),
]
