
from django.contrib import admin
from .views import *
from django.urls import path
urlpatterns = [
    path('discounts/<int:ordernumber>', discounts, name='discounts'),
    path('applyDiscount/', applyDiscount, name='applyDiscount')
]
