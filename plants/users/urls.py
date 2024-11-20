from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='reg'),
    path('login/', views.loginview, name ='login'),
    path('logout/', views.logoutview, name = 'logout')
]
