from django.contrib import admin
from django.urls import path, include
from crud1.views import login,home, interfaz_sa
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('crud1.urls')),  # Redirecciona la ruta vacía al login
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),  # Asegúrate de tener esta línea también si la necesitas
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)