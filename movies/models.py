from django.db.models import Model, ManyToManyField, CharField, IntegerField, TextField, EmailField, DateTimeField, \
    DecimalField


# Create your models here.


# Table: Movie , Actor
# Fields: Movie(Title, Actor, lenght, description),
#          Actor(Name, last_name),
# Sukurti views kurie galetu sukurti movie ar actor ir po sukurimo juos perkeltu i puslapi kuriame parodyti visi aktoriai ar filma priklauso nuo to ka sukure.


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
