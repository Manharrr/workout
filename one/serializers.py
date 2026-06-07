from rest_framework import serializers
from .models import Food,Hotel

class Hotelserializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields='__all__'

class Foodserializer(serializers.ModelSerializer):

    class Meta:
        model=Food
        fields='__all__'


# class Hotelserializer(serializers.ModelSerializer):

#     htl=Foodserializer(many=True)

#     class Meta:
#         model=Hotel
#         fields=['id','name','place','htl']