# Importamos las herramientas necesarias para crear clases abstractas
from abc import ABC,abstractmethod
# Definimos una clase abstracta llamada HistorialServicio
# Esta clase sirve como base para implementar un historial de servicios para una mascota
class HistorialServicio(ABC):
    # Declaramos un método abstracto que debe ser implementado por cualquier clase hija
    # Este método será responsable de agregar un servicio al historial
    @abstractmethod
    def agregar_servicio(self, servicio):
        pass
    # Declaramos otro método abstracto que también debe ser implementado por cualquier clase hija
    # Este método será el encargado de mostrar el historial de servicios realizados

    @abstractmethod
    def mostrar_historial(self):
        pass