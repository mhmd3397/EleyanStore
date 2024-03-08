from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['total_amount', 'notes', 'alternative_contact',
                  'communication_method', 'status']
