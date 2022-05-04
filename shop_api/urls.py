from django.urls import path
from .views import *

urlpatterns = [
    path('items/',ShopItems.as_view(),name='items'),
    path('items/<int:pk>/',ItemDetail.as_view()),
    path('soon/',ComingSoon.as_view()),
    path('soon/<int:pk>/',SoonDetail.as_view())
]