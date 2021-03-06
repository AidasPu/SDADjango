from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, EmailField, DateTimeField
from django.utils import timezone
from accounts.managers import UserUserManager


class CustomUser(AbstractUser):
    username = None
    email = EmailField('email', unique=True)
    warehouse = CharField(max_length=50)
    date_joined = DateTimeField(default=timezone.now())
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserUserManager()

    def __str__(self):
        return self.email
