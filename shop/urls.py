from django.contrib import admin
from django.urls import path

from config.urls import urlpatterns

urlpatterns = [
    path('', views.index, name='products'),
    path('detail/', views.product_detail, name='detail'),
]