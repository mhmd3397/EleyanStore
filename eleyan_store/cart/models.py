from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='cart')
    items = models.ManyToManyField(Product, through=CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __str__(self):
        return f'Cart of {self.user.username}'

    def total_price(self):
        return sum(item.get_total_price() for item in self.cartitem_set.all())

    def total_quantity(self):
        return sum(item.quantity for item in self.cartitem_set.all())
