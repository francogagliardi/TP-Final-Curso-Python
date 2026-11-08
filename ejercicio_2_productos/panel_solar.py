from dispositivo_ecologico import DispositivoEcologico


class PanelSolar(DispositivoEcologico): #Clase hija

    def __init__(self, id_producto, nombre, precio, stock, eficiencia, potencia_w): #Constructor
        super().__init__(id_producto, nombre, precio, stock)
        self.eficiencia = eficiencia
        self.potencia_w = potencia_w

    def generar_ficha_tecnica(self): #Funcion que devuelve un diccionario con los datos del panel solar
        ficha_tecnica = super().generar_ficha_tecnica() #Llamo a la funcion padre
        ficha_tecnica["eficiencia"] = self.eficiencia
        ficha_tecnica["potencia_w"] = self.potencia_w
        return ficha_tecnica #Mando la ficha tecnica 