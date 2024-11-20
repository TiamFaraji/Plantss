from .models import Addfield
from rest_framework.serializers import ModelSerializer

class dataserializer(ModelSerializer):
    class Meta:
        model = Addfield
        fields = '__all__'

    