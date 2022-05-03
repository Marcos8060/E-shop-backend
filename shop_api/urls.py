from django.urls import path
from .views import *

urlpatterns = [
    path('items/',ShopItems.as_view(),name='items')
]