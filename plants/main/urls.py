from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.newdef, name='list'),
    path('add-plants/', views.create, name = 'add')
]
