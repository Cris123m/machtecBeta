from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model=Service
        fields = ['title','description','photo','price','order']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'description':forms.Textarea(attrs={'class':'form-input'}),
            'photo':forms.ClearableFileInput(attrs={'class':'form-input'}),
            'price':forms.NumberInput(attrs={'class':'form-input'}),
            'order':forms.NumberInput(attrs={'class':'form-input'}),            
        }