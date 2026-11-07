def limpiar_registro_sensor(registro_raw): #Funcion encargada de estandarizar registros

    registro_procesado = {} #Diccionario donde se guardaran los datos estandarizados 
    claves_registro = list(registro_raw) #Lista de las claves del diccionario registro_raw
    no_ubicado = True #Variable para saber si esta cargada la ubicacion

    for clave in claves_registro: #Vario en funcion de las claves de registro_raw
        if clave == "sensor_id":
            registro_procesado[clave] = registro_raw[clave].strip() #Saco los espacios vacios del id
        elif clave == "temperatura":
            registro_procesado[clave] = float(registro_raw[clave].replace("C", "").replace("c", "").strip()) #Remplazo la "C" y la "c", saco los espacios y luego convierto en float
        elif clave == "ubicacion" and registro_raw[clave] != None and registro_raw[clave].strip() != "":
            no_ubicado = False #Anoto que hay ubicacion
            registro_procesado[clave] = registro_raw[clave].strip() #La guardo en el registro normalizado

    if no_ubicado: #En caso de no haber ubicacion
        registro_procesado["ubicacion"] = "No ubicado"

    return registro_procesado #Devuelvo el registro normalizado

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura): #Funcion que encuentra sensores que pasan cierto umbral y la temperatura promedio

    lista_sensores_alerta = [] #Aqui se guardaran los ID de los sensores que pasen el umbral
    sumatoria_temperatura = 0; #Aqui se sumaran todas las temperaturas de los sensores

    for sensor in lista_sensores_limpios: #Vario sensor a sensor
        if sensor["temperatura"] > umbral_temperatura: #Veo si la tremperatura se pasa del umbral
            lista_sensores_alerta.append(sensor["sensor_id"]) #Anoto el ID del sensor que se paso
        sumatoria_temperatura += sensor["temperatura"] #Sumo la temperatura del sensor para luego promediar

    return (lista_sensores_alerta, sumatoria_temperatura/len(lista_sensores_limpios)) #Retorno una tupla con la lista de sensores en alerta y con el promedio de temperatura