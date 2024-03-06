# products/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Product, Order, OrderItem, UserProfile, ProductReview
from .forms import OrderForm, UserProfileForm


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(
        user=request.user.userprofile, status='pending')
    order_item, item_created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if not item_created:
        order_item.quantity += 1
        order_item.save()

    messages.success(request, f"{product.name} added to your cart.")
    return redirect('cart')


@login_required
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order = Order.objects.get(user=request.user.userprofile, status='pending')
    order_item = OrderItem.objects.get(order=order, product=product)
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()

    messages.info(request, f"{product.name} removed from your cart.")
    return redirect('cart')


@login_required
def view_cart(request):
    order = Order.objects.get(user=request.user.userprofile, status='pending')
    return render(request, 'view_cart.html', {'order': order})


@login_required
def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.get(
                user=request.user.userprofile, status='pending')
            order.status = 'confirmed'
            order.save()

            messages.success(
                request, 'Your order has been confirmed. Thank you!')
            return redirect('order_confirmation')
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {'form': form})


@login_required
def order_confirmation(request):
    order = Order.objects.get(
        user=request.user.userprofile, status='confirmed')
    return render(request, 'order_confirmation.html', {'order': order})


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def edit_profile(request):
    return render(request, 'edit_profile.html')


@login_required
def product_management(request):
    return render(request, 'product_management.html')


@login_required
def order_management(request):
    orders = Order.objects.all()
    return render(request, 'order_management.html', {'orders': orders})


@login_required
def user_management(request):
    users = UserProfile.objects.all()
    return render(request, 'user_management.html', {'users': users})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(
                request, 'You have successfully registered and logged in.')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
