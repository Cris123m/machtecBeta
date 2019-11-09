from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import Photo
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PhotoForm

# Create your views here.
class PhotosListView(ListView):
    model = Photo

class PhotoDetailView(DetailView):
    model = Photo

class PhotoCreate(CreateView):
    model = Photo
    form_class=PhotoForm
    success_url=reverse_lazy('photos')

class PhotoUpdate(UpdateView):
    model = Photo
    form_class=PhotoForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id])+"?ok"

class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photos')