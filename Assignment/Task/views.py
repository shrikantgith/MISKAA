from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Create your views here.
#here we have this class will get called when we hit get and post 
#here it will automat. will convert complaxdata->pythondata->jsondata and reverce
#herer we have combine get and post bec. in both we dont need to pass id

class RPCartapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    # fetching all data complexdata 
    queryset =Cart.objects.all()
    #PASSING  to serializer to convert it into python data and than to json
    serializer_class = CartSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self, request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
#here we have combined get/id update and delete bec we need to pass id here to get
#specifick data  here it will automatically process all 
class RUDCartapi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset =Cart.objects.all()
    serializer_class = CartSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



    