from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    path('list/', views.plants_list.as_view(), name='list'),
    path('plant/<pk>', views.plant.as_view(), name='edit'),
]
