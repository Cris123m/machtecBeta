from django.urls import path
from .views import PhotosListView, PhotoDetailView, PhotoCreate, PhotoUpdate, PhotoDelete
from . import views

urlpatterns = [
    path('', PhotosListView.as_view(), name='photos'),
    path('<int:pk>/<slug:slug>/', PhotoDetailView.as_view(), name='photo'),
    path('create/',PhotoCreate.as_view(),name="createph"),
    path('update/<int:pk>/',PhotoUpdate.as_view(),name="updateph"),
    path('delete/<int:pk>/',PhotoDelete.as_view(),name="deleteph"),
]