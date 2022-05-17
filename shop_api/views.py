from django.shortcuts import render
from rest_framework import generics
from .models import  Item
from .models import  Special as SpecialModel
from .serializer import *

# Create your views here.

class ShopItems(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveAPIView):
      queryset = Item.objects.all()
      serializer_class = ItemSerializer

class Special(generics.ListCreateAPIView):
    queryset = SpecialModel.objects.all()
    serializer_class = SpecialSerializer

class SpecialDetail(generics.RetrieveAPIView):
      queryset = SpecialModel.objects.all()
      serializer_class = SpecialSerializer
