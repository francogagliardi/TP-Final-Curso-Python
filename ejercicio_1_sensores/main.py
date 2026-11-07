import sensores

lista_sensores_raw = [
    {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C",
        "ubicacion": "Planta Norte"
    },
    {
        "sensor_id": "SENSOR-002",
        "temperatura": " 31.8 C ",
        "ubicacion": "Deposito Central"
    },
    {
        "sensor_id": "  SENSOR-003 ",
        "temperatura": "18.0",
        "ubicacion": ""  # Ubicación vacía (cadena de espacios o vacía)
    },
    {
        "sensor_id": "SENSOR-004  ",
        "temperatura": "29.2c",
        # Falta la clave 'ubicacion'
    },
    {
        "sensor_id": " SENSOR-005 ",
        "temperatura": " 35.1C",
        "ubicacion": "  Planta Sur  "
    },
    {
        "sensor_id": "SENSOR-006",
        "temperatura": "22.4",
        "ubicacion": None  # Valor Nulo
    }
]

def main(lista_sensores_raw):
    print("Lista de sensores con regsistros sucios: ")
    mostrar_sensores(lista_sensores_raw)

    lista_sensores_limpios = [] #Arreglo dendo estaran los sensores limpios
    for sensor in lista_sensores_raw: #Vario en funcion de los sensores
        lista_sensores_limpios.append(sensores.limpiar_registro_sensor(sensor)) #Limpio el registro del sensor y lo guardo en la lista limpia
    print("Lista de sensores con registros estandarizados: ")
    mostrar_sensores(lista_sensores_limpios)

    temperatura_max = 25 #El umbral maximo de temperatura de los sensores antes de estar en alerta
    reporte = sensores.generar_resumen_sensores(lista_sensores_limpios, temperatura_max) #Genero reporte de sensores
    print(f"Lista de sensores en alerta:\n {reporte[0]}")
    print(f"La temperatura promedio de los sensores es:\n {reporte[1]}")


def mostrar_sensores(lista_sensores):
    num_sensor = 1
    for sensor in lista_sensores:
        print(f"Sensor ({num_sensor}):")
        print(sensor)
        num_sensor += 1


if __name__ == "__main__":
    main(lista_sensores_raw)