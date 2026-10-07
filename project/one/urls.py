from django.urls import path,include
from .views import Hotelapiview,HotelDetailed,Foodapiview

urlpatterns = [
    
    path('hotel/',Hotelapiview.as_view()),
    path('hotel/<int:pk>/',HotelDetailed.as_view()),
    path('food/',Foodapiview.as_view()),
    path('food/<int:pk>/',Foodapiview.as_view()),
]
