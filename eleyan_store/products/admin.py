from django.contrib import admin
from .models import Product, Category, Feature


class FeatureInline(admin.TabularInline):
    model = Product.features.through
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity',
                    'hide_product', 'hide_quantity']
    list_filter = ['hide_product', 'category']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FeatureInline]
    exclude = ('features',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Feature)
