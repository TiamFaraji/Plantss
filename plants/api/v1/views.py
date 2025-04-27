from main.serializers import dataserializer
from main.models import Addfield
from rest_framework import mixins, generics
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated

# region comment
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response 
# from rest_framework.decorators import api_view
# from rest_framework import status

# @api_view(['GET'])
# def plants_list(request):
# #     pl = Addfield.objects.all()
# #     serializer = dataserializer(pl, many=True)
# #     return Response(serializer.data, status.HTTP_200_OK)

# @api_view(['GET', 'PUT', 'DELETE'])
# def plant(request, plants_id):
#     pl = get_object_or_404(Addfield, id=plants_id, author=request.user)
#     if request.method == 'GET':
#         serializer = dataserializer(pl)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = dataserializer(pl, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(user=request.user)
#         return Response(serializer.data, status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         pl.delete()
#         response ={
#             'detail' : 'plant has been deleted'
#         }
#         return Response(response, status.HTTP_204_NO_CONTENT)
    
#endregion

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