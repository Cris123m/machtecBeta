from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields = ['title','content','order','photo']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'order':forms.NumberInput(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
        }