from django.contrib import admin
from django.urls import path

from plant import views


app_name = 'plant'

urlpatterns = [
    path('plant-detail/<str:name>/', views.plant_detail, name='plant_detail'),
    path('category/', views.plant_category, name='plant_category'),
    path('plant-family/<str:name>/', views.plant_family, name='plant_family'),
    # path('create_data/', views.test),
]
