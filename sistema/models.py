
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices


# Create your models here.

class clientes(models.Model):
	
	nombre = models.CharField(max_length=40)
	identificación = models.IntegerField(primary_key=True, unique=True)
	teléfono = models.IntegerField(blank=True, null=True)
	fecha_nacimiento = models.DateField(blank=True)
	email = models.EmailField(max_length=40, blank=True, null=True)
	publish_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'cliente'
		verbose_name_plural = 'clientes'

	def __str__(self):
		return self.nombre

class habitaciones(models.Model):

	codigo = models.IntegerField(primary_key=True, auto_created = True)

	HABITACIONES = Choices (

		('INDIVIDUAL', _('Individual')),
		('DOBLE DE USO INDIVIDUAL', _('Doble de Uso Individual')),
		('DOBLE', _('Habitación Doble')),
		('CON CAMA SUPLETORIA', _('Con cama Supletoria')),
		('TRIPLE', _('Habitación Triple')),
		('JUNIOR SUITE', _('Junior Suite')),
		('SUITE', _('Suite')),
		('SUITE NUPCIAL', _('Suit Nupcial')),
	)

	tipo_habitacion = models.CharField (max_length=25, choices=HABITACIONES)
	imagen = models.ImageField(null=True)

	precio = models.IntegerField(default = 0)
	cupo = models.BooleanField(default=True)
	nro_habitacion = models.IntegerField() 
	caracteristicas = models.TextField(blank=True,help_text='Descripción de la habitacion')

	created = models.DateTimeField(auto_now_add=True, null=True)
	updated = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name = 'habitación'
		verbose_name_plural = 'habitaciones'

	def __str__(self):
		return self.tipo_habitacion

class reservas (models.Model):
	
	cod_reserva = models.IntegerField(primary_key=True, auto_created = True,)
	nombre = models.CharField(max_length=40, blank=True)
	correo = models.EmailField(max_length=40, null=True, blank=True)
	telefono = models.IntegerField(null=True)
	fecha_entrada = models.DateField()
	fecha_salida = models.DateField()
	fecha_creacion = models.DateTimeField(auto_now=True)
	habitacion = models.ForeignKey(habitaciones, on_delete= models.CASCADE)
	cant_adultos = models.IntegerField()
	cant_niños = models.IntegerField(null=True, blank=True)
	mensaje = models.TextField(blank=True,help_text='Escriba aqui si tiene alguna petición especial')
	total_reserva = models.IntegerField()

	class Meta:
		verbose_name = 'reserva'
		verbose_name_plural = 'reservas'

	def __str__(self):
		return self.nombre







