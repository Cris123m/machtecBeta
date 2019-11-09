from django.urls import path
from .views import HomePageView, AboutPageView, ProductPageView,ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/',  AboutPageView.as_view(), name="about"),
    path('products/',  ProductPageView.as_view(), name="products"),
    path('contact-us/',  ContactPageView.as_view(), name="contact-us"),
]