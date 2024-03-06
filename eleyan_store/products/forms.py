# products/forms.py
from django import forms
from .models import Order, UserProfile


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['notes', 'alternative_number', 'communication_methods']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'email_confirmed',
                  'phone_number_confirmed', 'is_admin']
