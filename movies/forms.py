from django.forms import ModelForm, ModelMultipleChoiceField

from movies.models import Movie, Actor


class ActorForm(ModelForm):
    class Meta():
        model = Actor
        fields = "__all__"


class MovieForm(ModelForm):
    class Meta():
        model = Movie
        fields = "__all__"
