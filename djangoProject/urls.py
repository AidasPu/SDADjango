"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies.views import Create_movie, Create_actor, ActorListView, MovieListView
from django.contrib.auth import views as user_views
from accounts.views import register, hello, index

urlpatterns = [
    path('accounts/login/', user_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', user_views.LogoutView.as_view(), name="logout"),
    path('register/', register, name="register"),
    path('admin/', admin.site.urls),
    path('hello/<word>/<word1>', hello),
    path('hello/<word>/', hello),
    path('hello/', hello),
    path('', index, name='index'),
    path('movie/create', Create_movie.as_view(), name="create_movie"),
    path('actor/create', Create_actor.as_view(), name="create_actor"),
    path('movie/list', MovieListView.as_view(), name="movie_list"),
    path('actor/list', ActorListView.as_view(), name="actor_list"),
]
