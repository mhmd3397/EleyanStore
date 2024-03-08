from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart
from .forms import CartAddProductForm


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('cart:cart_detail')
    else:
        form = CartAddProductForm()
    return render(request, 'add_product.html', {'form': form})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detail_cart.html', {'cart': cart})
