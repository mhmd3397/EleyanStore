from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm
    success_url = reverse_lazy('orders:order_created')
    template_name = 'create_order.html'


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(
                order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    return render(request, 'orders/order/create.html')


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order/detail.html', {'order': order})
