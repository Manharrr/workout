from django.urls import path
from . models import Food,Hotel

from .views import hotelapi,hoteldetailed


urlpatterns = [
    path('hotel/',hotelapi.as_view()),
    path('hotel/<int:pk>/',hoteldetailed.as_view()),
    
]