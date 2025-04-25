
# Clase para gestionar clientes
# Clase Cliente que gestiona los datos de los clientes y sus mascotas
class Cliente:
    # El método __init__ es el constructor, se ejecuta cuando se crea un nuevo objeto de tipo Cliente.
    # Recibe el nombre y el teléfono como parámetros para inicializar los atributos del cliente.
    def __init__(self, nombre, telefono):
        self.nombre = nombre # Asigna el nombre del cliente.
        self.telefono = telefono  # Asigna el teléfono del cliente.
        self.mascotas = []# Inicializa una lista vacía para almacenar las mascotas del cliente.
    # Método para agregar una mascota al cliente. Recibe un objeto de tipo Mascota y lo agrega a la lista de mascotas.
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
# Método especial __str__ que se ejecuta cuando se intenta convertir el objeto Cliente a una cadena de texto.
# Se utiliza principalmente para imprimir de forma legible el objeto Cliente.
    def __str__(self):
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}"
