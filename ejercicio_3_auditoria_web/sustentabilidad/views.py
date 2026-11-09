from django.shortcuts import render

from .emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request): #request contiene los datos de la peticion web del usuario
    registros_prueba = [
        {"planta": "Planta Norte", "consumo_kwh": 8500},
        {"planta": "Sector Luján de Cuyo", "consumo_kwh": 12400},
        {"planta": "Nave Maipú", "consumo_kwh": 12400}, 
        {"planta": "Depósito Godoy Cruz", "consumo_kwh": 3200},
        {"planta": "Planta Sur", "consumo_kwh": 9100},
    ]

    emisiones_totales, plantas_maximas = obtener_metricas_consumo(registros_prueba) 

    contexto = {
        "total_emisiones": emisiones_totales,
        "plantas_alerta": plantas_maximas
    }

    return render(request, 'sustentabilidad/panel.html', contexto)