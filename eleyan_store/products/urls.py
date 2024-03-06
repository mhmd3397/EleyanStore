from django.urls import path
from .views import home, product_list, product_detail, add_to_cart, remove_from_cart, view_cart, checkout, order_confirmation, profile, edit_profile, product_management, order_management, user_management, user_login, user_logout, user_register

app_name = 'products'

urlpatterns = [
    path('product-list/', product_list, name='product_list'),
    path('', home, name='home'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/',
         remove_from_cart, name='remove_from_cart'),
    path('cart/', view_cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('product_management/', product_management, name='product_management'),
    path('order_management/', order_management, name='order_management'),
    path('user_management/', user_management, name='user_management'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
]
