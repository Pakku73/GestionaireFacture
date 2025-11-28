from django import forms
from .models import Product
from datetime import date


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "expiration_date"]
        widgets = {
            "id": forms.TextInput(attrs={"readonly": "readonly"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "expiration_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
        
    def clean_expiration_date(self):
        exp_date = self.cleaned_data["expiration_date"]

        if exp_date < date.today():
            raise forms.ValidationError("La date de péremption ne peut pas être dans le passé.")

        return exp_date