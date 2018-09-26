from django import forms 
from .models import Suscriptor
from django.utils.translation import ugettext_lazy as _

class SusForm(forms.ModelForm):
    class Meta:
        model = Suscriptor
        fields= ['nombre', 'apellido', 'email']
        labels={
        'nombre':_('Escribe tu nombre'),
        'apellido':_('Escribe su apellido'),
        'email':_('Introduce tu correo')
        }
        widgets = {
            
        }