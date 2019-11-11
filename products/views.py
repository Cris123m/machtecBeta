from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm

# Create your views here.
class ProductsListView(ListView):
    model = Product    

class ProductDetailView(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    form_class=ProductForm
    success_url=reverse_lazy('products')

class ProductUpdate(UpdateView):
    model = Product
    form_class=ProductForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id])+"?ok"

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products')