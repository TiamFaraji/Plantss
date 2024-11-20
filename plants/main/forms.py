from django import forms
from .models import Addfield

class Form(forms.ModelForm):
    
    class Meta:
        model = Addfield
        fields = '__all__'
