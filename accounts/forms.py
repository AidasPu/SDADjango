from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser
from django.forms import ModelForm
from django.forms import CharField, DateField
from datetime import datetime


class CreateUserCustomForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)
