from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class SoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soon
        fields = '__all__'