from main.serializers import dataserializer
from main.models import Addfield
from rest_framework import mixins, generics
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated


# region mixins
class plants_listt(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Addfield.objects.all()
    serializer_class = dataserializer
    
    def get(self, request: Request):
        return self.list(request)

class plantt(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Addfield.objects.all()
    serializer_class = dataserializer

    def get(self, request: Request, pk):
        return self.retrieve(request)
    
    def put(self, request:Request, pk):
        return self.update(request)
    
    def delete(self, request:Request, pk):
        return self.destroy(request)

#endregion 

class plants_list(generics.ListAPIView):
    queryset = Addfield.objects.all()
    serializer_class = dataserializer

class plant(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Addfield.objects.all()
    serializer_class = dataserializer