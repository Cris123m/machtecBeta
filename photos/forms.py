from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields = ['title','content','order','photo']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control form-input'}),
            'content':forms.Textarea(attrs={'class':'form-control form-input'}),
            'order':forms.NumberInput(attrs={'class':'form-control form-input'}),            
            'photo':forms.ClearableFileInput(attrs={'class':'form-input'}),
        }