# Se define la clase Mascota
from historialMascota import HistorialMascota # Se importa la clase HistorialMascota
class Mascota:
    def __init__(self, nombre, especie, raza):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.historial = HistorialMascota()
        
        # Se define la representacion en cadena del objeto mascota
    def __str__(self): # Cuando se llama a la funcion str() se imprime la informacion de la mascota
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Raza: {self.raza}"