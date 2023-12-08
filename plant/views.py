from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .models import *
import pandas as pd


@login_required
def plant_detail(request, name):
    # 取出相应的植物
    plant = Plant.objects.get(name=name)
    # 需要传递给模板的对象
    context = {'plant': plant}
    return render(request, 'plant/plant_detail.html', context)


@login_required
def plant_category(request):
    families = Family.objects.all()
    context = {'families': families}
    return render(request, 'plant/plant_category.html', context)


@login_required
def plant_family(request, name):
    # 取出相应的植物
    family = Family.objects.get(name=name)
    plants = Plant.objects.filter(genus__family=family)
    # 需要传递给模板的对象
    context = {'plants': plants}
    return render(request, 'plant/plant_family.html', context)


# def create_data(request):
#     data = pd.read_excel('static/data/Plant.xlsx')
#     # 遍历 CSV 文件中的每一行，并创建相应的对象
#     for index, row in data.iterrows():
#         # 获取或创建相应的 Family 对象
#         family_name = row['family']  # 假设 CSV 中有 'family' 字段指代 Family 名称
#         family, created = Family.objects.get_or_create(name=family_name)

#         # 获取或创建相应的 Genus 对象，并关联到 Family
#         genus_name = row['genus']  # 假设 CSV 中有 'genus' 字段指代 Genus 名称
#         genus, created = Genus.objects.get_or_create(name=genus_name, family=family)

#         # 创建 Plant 对象
#         plant = Plant(
#             name=row['name'],
#             genus=genus,
#             location=row['location'],
#             introduction=row['introduction'],
#             image_path=row['image_path']
#         )
#         plant.save()

