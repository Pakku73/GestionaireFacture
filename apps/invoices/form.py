from django import forms
from .models import InvoiceItem

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ["product", "quantity"]
