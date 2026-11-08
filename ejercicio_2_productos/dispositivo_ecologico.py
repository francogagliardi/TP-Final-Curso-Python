from excepciones import StockInvalidoError


class DispositivoEcologico: #Clase Padre

    def __init__(self, id_producto, nombre, precio, stock): #Constructor
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock #Stock es privado y pasa por el setter para validarlo

    @property #Getter de stock
    def stock(self):
        return self.__stock

    @stock.setter #Setter de stock
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidoError(self.id_producto, self.nombre)
        self.__stock = nuevo_stock

    def generar_ficha_tecnica(self): #Funcion que devuelve un diccionario con los datos del producto
        ficha_tecnica = {}
        ficha_tecnica["id_producto"] = self.id_producto
        ficha_tecnica["nombre"] = self.nombre
        ficha_tecnica["precio"] = f"${self.precio:.2f}" #Convierto el precio a string y le dejo 2 decimales
        ficha_tecnica["stock"] = self.stock
        return ficha_tecnica #Mando la ficha tecnica 