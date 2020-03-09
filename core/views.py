from django.shortcuts import render
from django.views.generic.base import TemplateView, HttpResponse

# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/home.html"

class AboutPageView(TemplateView):
    template_name = "core/about.html"

class ProductPageView(TemplateView):
    template_name = "core/products.html"

class ContactPageView(TemplateView):
    template_name = "core/contact-us.html"

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")
def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response

#https://data-flair.training/blogs/django-sessions/