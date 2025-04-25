from datetime import datetime
# Clase que representa una Cita entre un cliente y su mascota para un servicio en una fecha específica

class Cita:
    # El constructor (__init__) recibe cliente, mascota, fecha y servicio para inicializar una cita
    def __init__(self, cliente, mascota, fecha, servicio):
        self.cliente = cliente# Asigna el cliente asociado a la cita.
        self.mascota = mascota # Asigna la mascota asociada a la cita.
        self.fecha = fecha # Asigna la fecha de la cita.
        self.servicio = servicio# Asigna el servicio que se realizará en la cita.
    # Método especial __str__ que devuelve una representación legible de la cita
    def __str__(self):
        return f"Cita: {self.fecha}, Cliente: {self.cliente.nombre}, Mascota: {self.mascota.nombre}, Servicio: {self.servicio}"
    from datetime import datetime
# Decorador que valida el formato de la fecha antes de crear la cita
def validar_fecha(func):
    def wrapper(*args, **kwargs):
        fecha = args[2]# Extrae la fecha (que es el tercer argumento)
        try:
            # Intenta convertir la fecha a un objeto datetime usando el formato especificado
            datetime.strptime(fecha, "%Y-%m-%d")
            return func(*args, **kwargs)
        except ValueError:
            print("Error: Formato de fecha incorrecto. Use YYYY-MM-DD.")
    return wrapper
class CitaFactory:
    @staticmethod# Aplica el decorador para validar el formato de la fecha antes de crear la cita
    @validar_fecha
    def crear_cita(cliente, mascota, fecha, servicio):
        # Crea una nueva instancia de Cita con los datos proporcionados
        return Cita(cliente, mascota, fecha, servicio)
