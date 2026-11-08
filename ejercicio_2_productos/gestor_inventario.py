import json


class GestorInventario: #Clase encargada de pasar los objetos a un archivo .json

    @staticmethod 
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        lista_dispositivos_diccionario = [] #Aqui guardare los dispositivos como diccionarios
        for dispositivo in lista_dispositivos: #Vario en funcion de los dispositivos y los transformo en diccionarios
            lista_dispositivos_diccionario.append(dispositivo.generar_ficha_tecnica())
        with open(ruta_archivo, "w", encoding="utf-8") as archivo: #Lo transformo a json
            json.dump(lista_dispositivos_diccionario, archivo, indent = 4, ensure_ascii = False)