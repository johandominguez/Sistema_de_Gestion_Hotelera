from django.shortcuts import render, redirect

from .models import habitaciones
from .forms import formulario_contacto, ReservaForm

from django.core.mail import EmailMessage


# Create your views here.

def inicio(request):

	return render(request, 'sistema/inicio.html')

def habitaciones_list(request):

	habitacion = habitaciones.objects.all()
	return render (request, 'sistema/habitaciones.html' , {'habitacion': habitacion}) 
	
def reserva_form(request):

	form_reserva = ReservaForm(request.POST or None)

	if form_reserva.is_valid():
			form_reserva.save()
			form_reserva = ReservaForm

	context = {
			'form_reserva': form_reserva
		}

	return render(request, 'sistema/reserva.html', context )

def contacto_form(request):

	formulario = formulario_contacto()

	if request.method=="POST":
		
		formulario=formulario_contacto(data=request.POST)

		if formulario.is_valid():

			nombre=request.POST.get('nombre')
			telefono=request.POST.get('telefono')
			email=request.POST.get('email')
			mensaje=request.POST.get('mensaje')

			correo=EmailMessage('Mensaje desde App Django', 'El usuario con nombre {} , teléfono {} y la dirección de correo {}, escribe lo siguiente:\n\n {}'.format(nombre,telefono,email,mensaje),'',['stevendomin03@gmail.com'],reply_to=[email])

			try:
				correo.send()
				return redirect("/contacto/?valido")

			except:
				return redirect("/contacto/?novalido")

	return render(request, 'sistema/contacto.html', {'formulariocontacto': formulario})