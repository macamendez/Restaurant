from django.shortcuts import render
from .models import Restaurant

def menu(request):
    return render(request, 'restaurant/menu.html', {})

# Create your views here.
