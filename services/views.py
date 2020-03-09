from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.views.generic.list import ListView
from .models import Service
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import ServiceForm
from django.http import HttpResponse

# Create your views here.
class ServicesListView(ListView):
    model = Service

class ServiceDetailView(DetailView):
    model = Service

class ServiceCreate(CreateView):
    model = Service
    form_class=ServiceForm
    success_url=reverse_lazy('services')

class ServiceUpdate(UpdateView):
    model = Service
    form_class=ServiceForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id])+"?ok"

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('services')
