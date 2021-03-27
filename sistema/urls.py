from django.urls import path
from sistema import views


urlpatterns = [

    path('',views.inicio, name='Inicio'),
    path('habitaciones',views.habitaciones_list, name='Habitaciones'),
    path('reserva',views.reserva_form, name='Reserva'),
    path('contacto/',views.contacto_form, name='Contacto'),

]

