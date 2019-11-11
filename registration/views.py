from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserCreationFormWithEmail
from django import forms
# Create your views here.
class SignUp(CreateView):
    form_class=UserCreationFormWithEmail
    #success_url=reverse_lazy('login')
    template_name='registration/signup.html'
    def get_success_url(self):
        return reverse_lazy('login')+"?ok"
    def get_form(self,form_class=None):
        form=super(SignUp, self).get_form()
        form.fields['username'].widget=forms.TextInput(attrs={"class":"form-input","placeholder":"Nombre de usuario"})
        form.fields['email'].widget=forms.EmailInput(attrs={"class":"form-input","placeholder":"Correo electronico"})
        form.fields['password1'].widget=forms.PasswordInput(attrs={"class":"form-input","placeholder":"Password"})
        form.fields['password2'].widget=forms.PasswordInput (attrs={"class":"form-input","placeholder":"Confirm password"})
        return form