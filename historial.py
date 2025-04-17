from abc import ABC,abstractmethod # Se importan las clases abstractas ABC y abstractmethod para definir los metodos abstractos

class HistorialServicio(ABC): # Se define la clase HistorialServicio como una clase abstracta   
    @abstractmethod
    def agregar_servicio(self, servicio):
        pass

    @abstractmethod # Se define el metodo mostrar_historial como un metodo abstracto
    def mostrar_historial(self):
        pass