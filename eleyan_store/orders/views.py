from django.shortcuts import render
from .models import Order
from .forms import OrderCreateForm
from django.urls import reverse_lazy
from django.views import generic


class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderCreateForm
    success_url = reverse_lazy('orders:order_created')
    template_name = 'create_order.html'
