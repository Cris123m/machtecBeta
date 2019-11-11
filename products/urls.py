from django.urls import path
from .views import ProductsListView, ProductDetailView, ProductCreate, ProductUpdate, ProductDelete
from . import views

urlpatterns = [
    path('', ProductsListView.as_view(), name='products'),
    path('<int:pk>/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    path('create/',ProductCreate.as_view(),name="create"),
    path('update/<int:pk>/',ProductUpdate.as_view(),name="update"),
    path('delete/<int:pk>/',ProductDelete.as_view(),name="delete"),
]