from   historial import HistorialServicio # Se importa la clase HistorialServicio para manejar el historial de servicios

class HistorialMascota(HistorialServicio): # Se crea la clase HistorialMascota que hereda de la clase HistorialServicio
    def __init__(self):
        self.servicios = []

    def agregar_servicio(self, servicio):# Se agrega un servicio al historial para la mascota y se actualiza el historial
        self.servicios.append(servicio)

    def mostrar_historial(self):
        if not self.servicios:
            print("No hay servicios registrados.")
        else:
            for servicio in self.servicios:
                print(f" - {servicio}")