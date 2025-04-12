from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()  # Fetch all products from the DB
    return render(request, 'store/home.html', {'products': products})
