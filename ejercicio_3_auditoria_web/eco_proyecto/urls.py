from django.contrib import admin
from django.urls import path
from sustentabilidad.views import vista_panel_sustentabilidad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista_panel_sustentabilidad), #La raiz abre el panel, asi funciona la URL que muestra Django
    path('panel/', vista_panel_sustentabilidad), #Ruta directa al panel
]