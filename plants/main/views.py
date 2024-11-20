from django.shortcuts import render, redirect
from .models import Addfield
from . import forms

# Create your views here.

def newdef(request):
    new = Addfield.objects.all()
    return render(request, 'new/home.html',{'new':new})



def create(request):
    if request.method == 'POST':
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('api:list')
    form = forms.Form()
    return render(request, 'new/add-plant.html', {'form':form})

