from dispositivo_ecologico import DispositivoEcologico
from excepciones import StockInvalidoError
from gestor_inventario import GestorInventario
from panel_solar import PanelSolar


def main():
    catalogo_productos = []
    #Prueba de manejo de excepcion con stock negativo
    try:
        d_error = DispositivoEcologico("DEV-000", "Sensor Defectuoso", 15.00, -5)
        d_error.generar_ficha_tecnica() #No se va a alcanzar a ejecutar, lo pongo para sacar la advertencia en amarillo
    except StockInvalidoError as e:
        print(f"Excepcion capturada exitosamente: {e}")

    #Creo dispositivos validos
    d1 = DispositivoEcologico("DEV-001", "Aerogenerador Doméstico 500W", 450.00, 12)
    d2 = DispositivoEcologico("DEV-002", "Controlador de Carga MPPT 30A", 85.50, 25)
    d3 = DispositivoEcologico("DEV-003", "Inversor Onda Pura 2000W", 310.00, 8)
    d4 = DispositivoEcologico("DEV-004", "Sensor de Calidad de Aire IoT", 42.00, 50)
    d5 = DispositivoEcologico("DEV-005", "Batería Ciclo Profundo 100Ah", 210.00, 15)
    d6 = DispositivoEcologico("DEV-006", "Temporizador de Riego Solar", 35.00, 30)

    catalogo_productos.extend([d1, d2, d3, d4, d5, d6]) #Agrego los dispositivos a la lista

    #Creo paneles solares
    p1 = PanelSolar("SOL-101", "Panel Policristalino 160W", 120.00, 20, "17.5%", 160)
    p2 = PanelSolar("SOL-102", "Panel Monocristalino PERC 400W", 280.00, 14, "21.0%", 400)
    p3 = PanelSolar("SOL-103", "Panel Bifacial 550W", 410.50, 6, "22.8%", 550)
    p4 = PanelSolar("SOL-104", "Panel Flexible Portátil 100W", 95.00, 18, "19.2%", 100)

    catalogo_productos.extend([p1, p2, p3, p4]) #Agrego los paneles a la lista

    #Creo el archivo json con los datos de los dispositivos (Si ya esta creado borrarlo para comprobar el funcionamiento)
    ruta_archivo = "catalogo_ecotech.json"
    GestorInventario.guardar_catalogo_json(catalogo_productos, ruta_archivo)

if __name__ == "__main__":
    main()