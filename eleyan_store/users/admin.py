from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number',
                    'address', 'city', 'village', 'detailed_address']
    search_fields = ['username', 'email']
