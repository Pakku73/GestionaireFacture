from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .form import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"
    paginate_by = 10

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/form.html"
    success_url = reverse_lazy("products:list")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/form.html"
    success_url = reverse_lazy("products:list")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/delete.html"
    success_url = reverse_lazy("products:list")

