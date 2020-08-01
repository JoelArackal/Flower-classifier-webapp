from django import forms
from .models import Flowers

class Flowers_Form(forms.ModelForm):
    
    class Meta:
        model = Flowers
        fields = ('flower_image','id',)