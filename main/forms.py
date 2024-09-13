# main/forms.py
from django import forms
from .models import Usuario, Carrito

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo_electronico', 'contraseña']

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['nombre_producto', 'precio', 'cantidad']
