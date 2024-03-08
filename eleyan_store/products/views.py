from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.filter(hide_product=False)
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug)
    if product.hide_product:
        return render(request, 'product_not_available.html', {'product': product})
    return render(request, 'product_detail.html', {'product': product})
