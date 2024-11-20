from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Addfield(models.Model):
    name = models.CharField(max_length=30, verbose_name='english name')
    nameF = models.CharField(max_length=30, null=True, verbose_name='name')
    ittype = models.CharField(max_length=30, verbose_name='type')
    country = models.CharField(max_length=30, verbose_name='country')
    medical = models.BooleanField(verbose_name='medical')
    home = models.BooleanField(verbose_name='home')
    mainimage = models.ImageField(default='fallback.png', blank=True, verbose_name='main image')
    image1 = models.ImageField(default='fallback.png', blank=True, verbose_name='image1')
    image2 = models.ImageField(default='fallback.png', blank=True, verbose_name='image2')
    image3 = models.ImageField(default='fallback.png', blank=True, verbose_name='image3')
    sunlight = models.CharField(max_length=20,verbose_name='sunlight')
    humidity = models.CharField(max_length=20,verbose_name='humidity')
    temprature = models.CharField(max_length=20,verbose_name='temprature')
    amount = models.IntegerField(null=True, verbose_name='amount')
    discount = models.IntegerField(null=True, verbose_name='discount')
    store = models.CharField(max_length=30, verbose_name='store')
    suggestionplants = models.CharField(max_length=30, verbose_name='suggestionplants')
    introduction = models.TextField(max_length=500, verbose_name='introduction')
    description = models.TextField(max_length=2000, verbose_name='description')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='user')

    def __str__(self):
        return self.name
