from django import forms
from .models import Products

class ProductuploadForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        
        
        