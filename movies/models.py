from django.db.models import Model, ManyToManyField, CharField, IntegerField, TextField, EmailField, DateTimeField, \
    DecimalField

class Actor(Model):
    name = CharField(max_length=20)
    last_name = CharField(max_length=20)

    def __str__(self):
        return self.name + '' + self.last_name


class Movie(Model):
    title = CharField(max_length=30)
    lenght = IntegerField(verbose_name="Lenght in seconds")
    description = TextField(max_length=1000)
    actors = ManyToManyField(Actor)
