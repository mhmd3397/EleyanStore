# products/urls.py
from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', home, name='home'),
    path('product-list/', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/',
         remove_from_cart, name='remove_from_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order-confirmation/', order_confirmation, name='order_confirmation'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('product-management/', product_management, name='product_management'),
    path('order-management/', order_management, name='order_management'),
    path('user-management/', user_management, name='user_management'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
]
