from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

# Create your views here.

class ShopItems(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveAPIView):
      queryset = Item.objects.all()
      serializer_class = ItemSerializer


class ComingSoon(generics.ListCreateAPIView):
    queryset = Soon.objects.all()
    serializer_class = SoonSerializer


class SoonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soon.objects.all()
    serializer_class = SoonSerializer
