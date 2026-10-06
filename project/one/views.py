from django.shortcuts import render

# Create your views here.
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Hotel,Food
from .serializer import Hotelserializer,foodserializer

class Hotelapiview(APIView):
    def get(self,request):
        hotel=Hotel.objects.all()
        serializer=Hotelserializer(hotel,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
       hotel=Hotel.objects.get(id=pk)
       serializer= Hotelserializer(hotel,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
       return Response(serializer.errors)
    def post(self,request):
        serializer=Hotelserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class HotelDetailed(APIView):
    def get(self,request,pk):
        hotel=Hotel.objects.get(id=pk)
        serializer=Hotelserializer(hotel)
        return Response(serializer.data)
    
    def put(self,request,pk):
        serializer=Hotelserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        hotel=Hotel.objects.get(id=pk)
        hotel.delete()
        return Response({"mesg":" hotel deleted "})
        
class Foodapiview(APIView):
    def get(self,request,pk=None):
        if pk:
            food=Food.objects.get(id=pk)
            serializer=foodserializer(food)
           
        else:
            food=Food.objects.all()
            serializer=foodserializer(food,many=True)
        return Response(serializer.data)
