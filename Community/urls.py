from django.contrib import admin
from django.urls import path

from Community import views


app_name = 'community'

urlpatterns = [
    path("", views.loginORregister),
    path("login/", views.loginORregister),
    path("logout/", views.logout, name='logout'),
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]
