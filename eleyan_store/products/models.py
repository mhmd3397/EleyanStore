# products/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

COMMUNICATION_METHOD_CHOICES = [
    ('whatsapp_message', _('WhatsApp Message')),
    ('whatsapp_call', _('WhatsApp Call')),
    ('regular_call', _('Regular Call')),
    ('regular_message', _('Regular Message')),
]


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(
        _('Phone Number'), max_length=15, unique=True)
    email_confirmed = models.BooleanField(_('Email Confirmed'), default=False)
    phone_number_confirmed = models.BooleanField(
        _('Phone Number Confirmed'), default=False)
    is_admin = models.BooleanField(_('Admin'), default=False)


class Category(models.Model):
    name = models.CharField(_('Category Name'), max_length=100)

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    name = models.CharField(_('Characteristic Name'), max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('Product Name'), max_length=100)
    description = models.TextField(_('Description'))
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField(
        _('Quantity Available'), blank=True, null=True)
    categories = models.ManyToManyField(Category, verbose_name=_('Categories'))
    characteristics = models.ManyToManyField(
        Characteristic, verbose_name=_('Characteristics'))
    is_quantity_limited = models.BooleanField(
        _('Is Quantity Limited'), default=False)
    is_characteristic_required = models.BooleanField(
        _('Is Characteristic Required'), default=False)
    image = models.ImageField(
        _('Product Image'), upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address_state = models.CharField(_('State'), max_length=100)
    address_city = models.CharField(_('City'), max_length=100)
    address_village = models.CharField(_('Village'), max_length=100)
    address_street = models.CharField(_('Street'), max_length=100)
    is_default = models.BooleanField(_('Default Address'), default=False)

    def __str__(self):
        return f"{self.address_state}, {self.address_city}, {self.address_street}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('confirmed', _('Confirmed')),
        ('canceled', _('Canceled')),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product, through='OrderItem', verbose_name=_('Products'))
    addresses = models.ManyToManyField(
        UserAddress, verbose_name=_('Addresses'))
    notes = models.TextField(_('Notes'), blank=True)
    alternative_number = models.CharField(
        _('Alternative Number'), max_length=15, blank=True)
    communication_methods = models.ManyToManyField(
        'CommunicationMethod', verbose_name=_('Communication Methods'))
    status = models.CharField(
        _('Status'), max_length=20, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField(
        _('Order Total'), max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.user.user.username}"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_('Quantity'))
    notes = models.TextField(_('Notes'), blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(_('Rating'), default=5)
    review_text = models.TextField(_('Review Text'))
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.user.username} for {self.product.name}"


class CommunicationMethod(models.Model):
    name = models.CharField(_('Method Name'), max_length=100,
                            choices=COMMUNICATION_METHOD_CHOICES)

    def __str__(self):
        return self.name
