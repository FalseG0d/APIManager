from django.forms import ModelForm
from .models import ImageModel
from django import forms

class ImageForm(ModelForm):
    image = forms.ImageField()
    class Meta:
        model=ImageModel
        fields='__all__'