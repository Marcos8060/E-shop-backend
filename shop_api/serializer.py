from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = '__all__'

class RandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Random
        fields = '__all__'


class AccesorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'