class StockInvalidoError(Exception): #Excepcion personalizada para el stock

    def __init__(self, id_producto, nombre, mensaje = "El stock no puede ser un valor negativo"):
        self.id_producto = id_producto
        self.nombre = nombre
        self.mensaje = f"Error en {nombre} con id {id_producto} : {mensaje}"
        super().__init__(mensaje)