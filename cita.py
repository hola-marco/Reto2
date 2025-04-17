from datetime import datetime # Se importa la clase datetime para trabajar fechas y horas de la cita

class Cita:
    def __init__(self, cliente, mascota, fecha, servicio):
        #Metodo constructor de la clase cita que recibe como argumentos el cliente, la mascota, la fecha y el servicio
        self.cliente = cliente
        self.mascota = mascota
        self.fecha = fecha
        self.servicio = servicio

    def __str__(self):
        # Este es un metodo para mostrar la informacion de la cita en la cadena de texto
        return f"Cita: {self.fecha}, Cliente: {self.cliente.nombre}, Mascota: {self.mascota.nombre}, Servicio: {self.servicio}"

def validar_fecha(func):
    #Este es un decorador que valida el formato de la fecha antes de ejecutar la función.
    def wrapper(*args, **kwargs):
        fecha = args[2]
        try:
            # Se valida el formato correcto para el formato YYYY-MM-DD usando la libreria datetime.strptime
            datetime.strptime(fecha, "%Y-%m-%d")
            return func(*args, **kwargs)
        except ValueError:
            # Se imprime un mensaje de error en caso de que el formato de la fecha sea incorrecto
            print("Error: Formato de fecha incorrecto. Use YYYY-MM-DD.")
    return wrapper
class CitaFactory: # Se crea la clase CitaFactory para crear citas de manera sencilla como se muestra en el ejemplo
    @staticmethod
    @validar_fecha
    def crear_cita(cliente, mascota, fecha, servicio):
        return Cita(cliente, mascota, fecha, servicio)