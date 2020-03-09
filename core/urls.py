from django.urls import path
from .views import HomePageView, AboutPageView, ProductPageView,ContactPageView, cookie_session, cookie_delete

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/',  AboutPageView.as_view(), name="about"),
    path('contact-us/',  ContactPageView.as_view(), name="contact-us"),
    path('testcookie/', cookie_session),
    path('deletecookie/', cookie_delete),
]