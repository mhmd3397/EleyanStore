# products/admin.py
from django.contrib import admin
from .models import UserProfile, Category, Characteristic, Product, Order, OrderItem, CommunicationMethod

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Characteristic)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CommunicationMethod)
