from django.forms import ModelForm, CharField, DateTimeField, Textarea, EmailField, ChoiceField
from old_uers.models import User

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
