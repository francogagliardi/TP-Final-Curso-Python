def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4): #Funcion que calcula las emisiones de carbono
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")
    else:
        return consumo_kwh * factor_emision

def obtener_metricas_consumo(registros): #Recibe una lista de diccionarios que contienen nombre de la planta y consumo
    emision_total = 0 #Aqui acumulare las emisiones de las plantas
    gasto_max = registros[0]["consumo_kwh"] #Aqui estara la energia maxima gastada
    plantas_mayor_gasto = [] #Aqui estaran los nombres de las plantas que mas gastaron

    for planta in registros: #Vario en funcion de las plantas
        emision_total += calcular_emisiones_carbono(planta["consumo_kwh"]) #Sumo las emisiones de la planta al total
        if planta["consumo_kwh"] > gasto_max: #Veo si el gasto de la planta es mayor al gasto maximo registrado  # noqa: PLR1730
            gasto_max = planta["consumo_kwh"] #Actualizo el gasto mas grande

    for planta in registros: #Vario en funcion de las plantas
        if planta["consumo_kwh"] == gasto_max: #Veo si la planta esta entre las que mas gastaron
            plantas_mayor_gasto.append(planta["planta"]) #Registro su nombre en el arreglo de plantas que mas gastaron

    return (emision_total, plantas_mayor_gasto) #Retorno la emision total y las plantas con mayor gasto


