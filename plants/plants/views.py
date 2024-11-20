from django.shortcuts import render
from main.models import Addfield

def home(request):
    return render(request, 'first.html')