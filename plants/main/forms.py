from django import forms
from .models import Addfield
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class Form(forms.ModelForm):
    
    class Meta:
        model = Addfield
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2') 