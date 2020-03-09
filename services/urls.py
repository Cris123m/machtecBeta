from django.urls import path
from .views import ServicesListView, ServiceDetailView, ServiceCreate, ServiceUpdate, ServiceDelete
from . import views

urlpatterns = [
    path('', ServicesListView.as_view(), name='services'),
    path('<int:pk>/<slug:slug>/', ServiceDetailView.as_view(), name='service'),
    path('create/',ServiceCreate.as_view(),name="create"),
    path('update/<int:pk>/',ServiceUpdate.as_view(),name="update"),
    path('delete/<int:pk>/',ServiceDelete.as_view(),name="delete"),
]