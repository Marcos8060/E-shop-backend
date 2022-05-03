from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

# Create your views here.

class ShopItems(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
