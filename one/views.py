from django.shortcuts import render

from rest_framework .views import APIView
from rest_framework import response
from rest_framework import status

from .models import Hotel,Food
from .serializers import Hotelserializer,Foodserializer


class hotelapi(APIView):

    def get (self,request):
        hotel=Hotel.objects.all()

        serializer=Hotelserializer(hotel,many=True)

        return response(serializer.data)
    def post(self,request):
        serializer=Hotelserializer(data=request.data)

        if serializer.is_valid:
            serializer.save()

            return response(serializer.data,status=status.HTTP_201_CREATED)
        return response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class hoteldetailed(APIView):
    









