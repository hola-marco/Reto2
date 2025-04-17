from datetime import datetime  # Se Importa la clase datetime para manejar fechas

class Cita:
    def __init__(self, cliente, mascota, fecha, servicio):
        # Metodo Constructor de la clase Cita para inicializar los atributos de la cita.
        self.cliente = cliente 
        self.mascota = mascota  
        self.fecha = fecha  
        self.servicio = servicio  

    def __str__(self):
        # Este Método devuelve una cadena de texto con la información de la cita
        return f"Cita: {self.fecha}, Cliente: {self.cliente.nombre}, Mascota: {self.mascota.nombre}, Servicio: {self.servicio}"

def validar_fecha(func):
    # Este Decorador valida el formato de la fecha antes de ejecutar la función original
    def wrapper(*args, **kwargs):
        fecha = args[2] 
        try:
            # Se Valida convertir la fecha al formato YYYY-MM-DD usando la libreria datetime
            datetime.strptime(fecha, "%Y-%m-%d")
            return func(*args, **kwargs)  # Si es válida, Se ejecuta la función original
        except ValueError:
            # Se imprime un mensaje de error en caso de que el formato de la fecha sea incorrecto
            print("Error: Formato de fecha incorrecto. Use YYYY-MM-DD.")
    return wrapper  # Se retorna la funcion wrapper que contiene la logica de la validacion
class CitaFactory:
    @staticmethod
    @validar_fecha  # Se Aplica el decorador validar_fecha el metodo crear_cita
    def crear_cita(cliente, mascota, fecha, servicio):
        # Metodo 
        return Cita(cliente, mascota, fecha, servicio)  # Se retorna la instancia de la clase Cita