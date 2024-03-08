from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter the product category")

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter the product feature")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(
        upload_to='products/', blank=True, null=True, help_text="Upload the product image")
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE, help_text="Select the product category")
    features = models.ManyToManyField(
        Feature, related_name='products', help_text="Select the product features")
    hide_product = models.BooleanField(
        default=False, help_text="Check this box to hide the product")
    hide_quantity = models.BooleanField(
        default=False, help_text="Check this box to hide the product quantity")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
