from django.shortcuts import render
from .models import Product
from django.views import generic


class ProductListView(generic.ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
