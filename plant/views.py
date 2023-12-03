from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .models import *


@login_required
def plant_detail(request, name):
    # 取出相应的植物
    plant = Plant.objects.get(name=name)
    # 需要传递给模板的对象
    context = { 'plant': plant }
    return render(request, 'plant_detail.html', context)

