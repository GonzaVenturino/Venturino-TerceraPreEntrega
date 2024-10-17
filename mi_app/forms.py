from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
