from django.urls import path

from django.contrib.auth import views as user_views
from accounts.views import register, hello, index

app_name = "accounts"

urlpatterns = [
    path('login/', user_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', user_views.LogoutView.as_view(), name="logout"),
    path('register/', register, name="register"),
    path('hello/<word>/<word1>', hello),
    path('hello/<word>/', hello),
    path('hello/', hello),
    path('', index, name='index'),
]
