from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    categories = models.Categorie.objects.filter()
    drinks = models.DrinkMenu.objects.filter().all()
    return render(request, 'index.html', locals())