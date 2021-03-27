from django.contrib import admin
from django.contrib.admin.models import LogEntry
from sistema.models import clientes,habitaciones,reservas
# Register your models here.

class clientesAdmin(admin.ModelAdmin):

	list_display = ['identificación', 'nombre','teléfono','fecha_nacimiento', 'email', 'publish_date']
	search_fields = ['identificación', 'nombre']
	list_editable = ['nombre','teléfono','fecha_nacimiento','email']
	list_per_page = 10

class habitacionesAdmin(admin.ModelAdmin):

	#readonly_fields= ['created', 'updated']

	list_display = ['codigo', 'tipo_habitacion', 'precio','cupo','nro_habitacion']
	list_editable = ['cupo']

	search_fields = ['codigo', 'nro_habitacion']
	
	fields = [
		('nro_habitacion'),
		'tipo_habitacion','imagen','caracteristicas',
		('cupo', 'precio',)

	]

	list_filter = ('tipo_habitacion','nro_habitacion',)

	list_per_page = 10

class reservasAdmin(admin.ModelAdmin):

	fields = [('nombre','correo','telefono','fecha_entrada','fecha_salida','habitacion','cant_adultos','cant_niños','mensaje')]

	list_display = ['cod_reserva','nombre','correo','telefono','fecha_entrada','fecha_salida','habitacion','cant_adultos','cant_niños','mensaje','fecha_creacion']

	search_fields = ['cod_reserva',]

	list_filter = ('fecha_creacion',)
	date_hierarchy = 'fecha_creacion'
	list_per_page = 10


admin.site.register(clientes, clientesAdmin)
admin.site.register(habitaciones, habitacionesAdmin)
admin.site.register(reservas, reservasAdmin)

# ---Limpiar el panel de actividades recientes del administrador--

#LogEntry.objects.all().delete()