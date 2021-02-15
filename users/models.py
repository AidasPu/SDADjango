from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, DateTimeField, EmailField, Choices, TextField, DateField


class User(Model):
    name = CharField(max_length=50)
    last_name = CharField(max_length=50, null=True)
    email = EmailField(max_length=50, null=True)
    gender = CharField(verbose_name='gender', max_length=15, choices=[('male', 'male'),('female', 'female')], null=True)
    description = TextField("Description about you ", max_length=255, null=True)
    created = DateTimeField(auto_now_add=True)

class Lobby(Model):
    title = CharField(max_length=30)
    user = ForeignKey(User, on_delete=DO_NOTHING)
    created = DateTimeField(auto_now_add=True)
