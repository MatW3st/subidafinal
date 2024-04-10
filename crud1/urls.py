from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from crud1.views import home, login
from django.urls import path, include
from django.contrib import admin
from django.urls import path




urlpatterns = [    
    path('', views.home, name='home'),  # Esta línea configura la URL para la página de inicio
    
    #Ajax
    ##
    path('login/', views.login, name='login'),
    path('interfaz_sa', views.interfaz_sa, name='interfaz_sa'),
    path('interfaz_ta/', views.interfaz_ta, name='interfaz_ta'),
    path('guardar_usuario/', views.guardar_usuario, name='guardar_usuario'),
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('peliculas/', views.peliculas, name= 'peliculas'), 
    path('eliminar_pelicula/', views.eliminar_pelicula, name='eliminar_pelicula'),


    path('editar_pelicula/<int:pelicula_id>/', views.editar_pelicula, name='editar_pelicula'),
    path('menu/', views.menu, name='menu'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
