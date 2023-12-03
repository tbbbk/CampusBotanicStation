from django.contrib import admin
from django.urls import path

from plant import views


app_name = 'plant'

urlpatterns = [
    path('plant-detail/<str:name>/', views.plant_detail, name='plant_detail'),
]
