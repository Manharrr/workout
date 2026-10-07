from rest_framework import serializers
from .models import Hotel,Food

class Hotelserializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields=['name','place']

class foodserializer(serializers.ModelSerializer):
    hotel=Hotelserializer()


    class Meta:
        model=Food
        fields='__all__'

  
