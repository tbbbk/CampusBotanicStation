from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from plant.models import *

@login_required
def index(request):
    recommdations = Recommendation.objects.all()
    context = {'recommendations': recommdations}
    for recommendation in recommdations:
        print(recommendation.plant.image_path)
    return render(request, 'index.html', context)