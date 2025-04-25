# Importamos las clases necesarias desde otros módulos:
from cliente import Cliente # - Cliente: para manejar la información de los clientes
from mascota import Mascota # - Mascota: para gestionar los datos de las mascotas.
from cita import CitaFactory# - CitaFactory: para crear objetos de tipo Cita de forma controlada.
# Importamos también módulos estándar de Python:
import json # - json: para leer y escribir archivos en formato JSON (guardar y cargar datos).

from os import path# - path (desde os): para comprobar si existen archivos o rutas (útil al cargar datos guardados).

class Veterinaria:
    def __init__(self):
        self.clientes = []        # Lista para almacenar los clientes registrados
        self.citas = []  # Lista para almacenar las citas programadas

    def agregar_cliente(self, cliente):
        if any(c.nombre == cliente.nombre for c in self.clientes): # Verifica si ya existe un cliente con el mismo nombre
            print("Error: Ya existe un cliente con ese nombre.")
        else:
            self.clientes.append(cliente)            # Si no existe, lo agrega a la lista de clientes
            print(f"Cliente {cliente.nombre} registrado con éxito.")

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:    # Recorre la lista de clientes buscando por nombre
            if cliente.nombre == nombre:
                return cliente# Retorna el cliente si lo encuentra
        print("Error: Cliente no encontrado.")
        return None # Retorna None si no se encuentra el cliente

    def agregar_cita(self, cita):
        self.citas.append(cita)    # Agrega la cita a la lista de citas
        print(f"Cita para {cita.mascota.nombre} registrada con éxito.")

    def cancelar_cita(self, fecha, nombre_mascota):
        cita_a_cancelar = None
        for cita in self.citas:    # Busca la cita que coincide con la fecha y el nombre de la mascota
            if cita.fecha == fecha and cita.mascota.nombre == nombre_mascota:
                cita_a_cancelar = cita
                break
        if cita_a_cancelar:# Si la encuentra, la elimina de la lista de citas
            self.citas.remove(cita_a_cancelar)
            print(f"Cita del {fecha} para {nombre_mascota} cancelada.")
        else:
            print("Error: Cita no encontrada.")        # Si no la encuentra, muestra un mensaje de error

    def mostrar_clientes(self):
        if not self.clientes:    # Verifica si la lista de clientes está vacía
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:        # Recorre cada cliente en la lista
                print(cliente)# Muestra los datos del cliente
            # Recorre y muestra las mascotas asociadas al cliente
                for mascota in cliente.mascotas:
                    print(f"  {mascota}")# Muestra los datos de cada mascota con sangría

    def mostrar_citas(self):
        if not self.citas:    # Verifica si hay citas en la lista
            print("No hay citas programadas.")
        else:
            for cita in self.citas:        # Recorre y muestra cada cita registrada
                print(cita)

    def guardar_datos(self, archivo):    # Construye un diccionario con los datos de clientes y citas
        datos = {
            "clientes": [ # establecimos diccionarios
                {
                    "nombre": c.nombre, # Nombre del cliente
                    "telefono": c.telefono, # Teléfono del cliente
                    "mascotas": [
                        {
                            "nombre": m.nombre,# Nombre de la mascota
                            "especie": m.especie, # Especie (ej. perro, gato)
                            "raza": m.raza, # Raza de la mascota
                            "historial": m.historial.servicios# Historial de servicios
                        }
                        for m in c.mascotas # Para cada mascota del cliente
                    ]
                }
                for c in self.clientes# Para cada cliente
            ],
            "citas": [
                {
                    "cliente": c.cliente.nombre, # Nombre del cliente de la cita
                    "mascota": c.mascota.nombre, # Nombre de la mascota
                    "fecha": c.fecha,# Fecha de la cita
                    "servicio": c.servicio # Servicio agendado
                }
                for c in self.citas  # Para cada cita
            ]
        }
        
    # Guarda el diccionario en un archivo JSON
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4) # indent=4 da formato legible
        print(f"Datos guardados en {archivo}.") # Confirmación de guardado

    def cargar_datos(self, archivo):    # Verifica si el archivo existe; si no, muestra error y termina
        if not path.exists(archivo):
            print("Error: Archivo no encontrado.")
            return
        with open(archivo, "r") as f:    # Abre y carga el contenido del archivo JSON en la variable 'datos'
            datos = json.load(f)
                # Reconstruye los objetos Cliente y sus mascotas

        for cliente_data in datos["clientes"]:
            cliente = Cliente(cliente_data["nombre"], cliente_data["telefono"])
            for mascota_data in cliente_data["mascotas"]:
                mascota = Mascota(mascota_data["nombre"], mascota_data["especie"], mascota_data["raza"])
                mascota.historial.servicios = mascota_data["historial"]
                cliente.agregar_mascota(mascota)            # Asocia la mascota al cliente
            self.clientes.append(cliente)        # Agrega el cliente completo a la lista de clientes
        for cita_data in datos["citas"]:
            cliente = self.buscar_cliente(cita_data["cliente"])
            if cliente:
                            # Busca la mascota del cliente por nombre
                mascota = next((m for m in cliente.mascotas if m.nombre == cita_data["mascota"]), None)
                if mascota:                # Crea la cita usando la fábrica
                    cita = CitaFactory.crear_cita(cliente, mascota, cita_data["fecha"], cita_data["servicio"])
                    if cita:
                        self.citas.append(cita)    # Agrega la cita a la lista de citas
        print(f"Datos cargados desde {archivo}.")