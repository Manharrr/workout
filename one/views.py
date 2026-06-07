from django.shortcuts import render

from rest_framework .views import APIView
# from rest_framework import response
from rest_framework import status
from rest_framework .response import Response

from .models import Hotel,Food
from .serializers import Hotelserializer,Foodserializer


class hotelapi(APIView):

    def get (self,request):
        hotel=Hotel.objects.all()

        serializer=Hotelserializer(hotel,many=True)

        return Response(serializer.data)
    def post(self,request):
        serializer=Hotelserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class hoteldetailed(APIView):

    def get(self,request,pk):
        hotel=Hotel.objects.get(id=pk)

        serializer=Hotelserializer(hotel)
        return Response(serializer.data)
    
    def put(self,request,pk):

        hotel=hotel.objects.get(id=pk)

        serializer=Hotelserializer(hotel,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        htl=Hotel.objects.get(id=pk)
        htl.delete()

        return Response('deletyed')
        
    
 



        pass
    
    









