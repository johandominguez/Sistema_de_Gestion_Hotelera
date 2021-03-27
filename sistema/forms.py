from django import forms
from django.forms import ModelForm
from .models import reservas


class formulario_contacto(forms.Form):

	nombre = forms.CharField(label = 'Nombre Completo', max_length = 30 )
	telefono = forms.CharField(label = 'Teléfono', max_length= 10, required =False)
	email = forms.EmailField(label = 'Correo electronico', max_length = 30)
	mensaje = forms.CharField(label = 'Mensaje', max_length= 100, widget=forms.Textarea)

class ReservaForm(forms.ModelForm):

	
	class Meta:
		model = reservas
		fields = ['nombre', 'correo', 'telefono', 'habitacion','fecha_entrada','fecha_salida', 'cant_adultos', 'cant_niños', 'mensaje']


