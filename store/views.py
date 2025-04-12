from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()  # Fetch all products from the DB
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'store/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Register view
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'store/register.html')