from django.urls import path
from .views import *

urlpatterns = [
    path('items/',ShopItems.as_view(),name='items'),
    path('items/<int:pk>/',ItemDetail.as_view()),
    path('special/',Special.as_view()),
    path('special/<int:pk>/',SpecialDetail.as_view()),
    path('random/',RandomModel.as_view()),
    path('accessory/',AcessoryModel.as_view()),
    path('accessory/<int:pk>/',AcessoryDetail.as_view()),
]