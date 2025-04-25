from veterinaria import Veterinaria # esta es el modulo veterianria ,importamos Veterinaria
from cliente import Cliente  # este es el modulo  cliente  importamos ala clase Cliente
from mascota import Mascota#  este es el modulo mascota ,de la clase Mascota
from cita import CitaFactory # este es el mdulo cita y importamos la clase Citafactory




def menu():
    # Se crea una instancia de la clase Veterinaria para manejar la lógica del sistema
    veterinaria = Veterinaria()
    # Se define el nombre del archivo donde se guardarán o leerán los datos en formato JSON
    archivo_datos = "veterinaria_data.json"
# Menú interactivo
    while True:
        print("\n----- BIENVENIDA A LA VETERINARIA HUELLA FELIZ -----")
        print("1. Registrar cliente")
        print("2. Registrar mascota")
        print("3. Gestion de citas")
        print("4. Historial")
        print("5. Salir")
        
        opcion = input("Seleccione una opcion: ")
# Finalmente, se agrega el cliente al sistema de la veterinaria usando el método agregar_cliente

        if opcion == "1":# Si el usuario elige la opción 1, se solicitan los datos del cliente
            nombre = input("Nombre del cliente: ")# Se piden el nombre y teléfono del cliente por consola
            telefono = input("Teléfono del cliente: ")
            cliente = Cliente(nombre, telefono)# Luego, se crea una instancia de la clase Cliente con esos datos
            veterinaria.agregar_cliente(cliente)# Finalmente, se agrega el cliente al sistema de la veterinaria usando el método agregar_cliente
        elif opcion == "2":# Si el usuario elige la opción 2, se registra una mascota a un cliente existente.

            nombre_cliente = input("Nombre del cliente: ")# Se solicita el nombre del cliente y se busca en el sistema usando buscar_cliente.

            cliente = veterinaria.buscar_cliente(nombre_cliente)
            if cliente:# Si el cliente existe:
                nombre_mascota = input("Nombre de la mascota: ")
                especie = input("Especie de la mascota: ")#   - Se piden los datos de la mascota: nombre, especie y raza.
                raza = input("Raza de la mascota: ")
                mascota = Mascota(nombre_mascota, especie, raza)#   - Se crea una instancia de la clase Mascota con esos datos.
                cliente.agregar_mascota(mascota)#   - Se agrega la mascota al cliente usando el método agregar_mascota.
                print(f"Mascota {nombre_mascota} registrada con éxito.")#   - Se muestra un mensaje de éxito.
            else:
                print("Error: Cliente no encontrado.")# Si el cliente no existe, se muestra un mensaje de error.

        elif opcion == "3":  # Si el usuario elige la opción 3, se muestra un submenú para la gestión de citas:            
            print("\n----- GESTION DE CITAS -----")
            print("1. Programar cita")
            print("2. Cancelar cita")
            print("3. Mostrar citas programadas")
            print("4. Mostrar clientes y mascotas")
            print("5. Volver al menu principal")
            
            sub_opcion = input("Seleccione una opcion: ")
            if sub_opcion == "1":# 1. Programar una cita:
                nombre_cliente = input("Nombre del cliente: ")
                cliente = veterinaria.buscar_cliente(nombre_cliente)#    - Se solicita el nombre del cliente y se busca en la veterinaria.

                if cliente:#    - Si el cliente existe, se pide el nombre de la mascota.
                    nombre_mascota = input("Nombre de la mascota: ")
                    mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
                    if mascota:#    - Se busca la mascota dentro del cliente.
                        fecha = input("Fecha de la cita (YYYY-MM-DD): ")#    - Si la mascota también existe, se pide la fecha y el servicio de la cita.
                        servicio = input("Servicio a realizar: ")
                        cita = CitaFactory.crear_cita(cliente, mascota, fecha, servicio)#    - Se crea la cita usando CitaFactory y se agrega a la veterinaria.
                        if cita:
                            veterinaria.agregar_cita(cita)
                    else:
                        print("Error: Mascota no encontrada.")
            elif sub_opcion == "2":# 2. Cancelar una cita:
                fecha = input("Fecha de la cita a cancelar (YYYY-MM-DD): ")#   Se solicita la fecha y el nombre de la mascota para cancelar la cita correspondiente.

                nombre_mascota = input("Nombre de la mascota: ")
                veterinaria.cancelar_cita(fecha, nombre_mascota)
            elif sub_opcion == "3":# 3. Mostrar citas programadas:
                veterinaria.mostrar_citas()#    - Se listan todas las citas registradas en el sistema.
            elif sub_opcion == "4":# 4. Mostrar clientes y mascotas:
                veterinaria.mostrar_clientes()#    - Se listan todos los clientes junto con sus mascotas.
            elif sub_opcion == "5":
                continue
            else:
                print("Opción no válida. Intente de nuevo.")

        elif opcion == "4":# Si el usuario elige la opción 4, se permite consultar el historial de servicios de una mascota.
            nombre_cliente = input("Nombre del cliente: ")# - Se solicita el nombre del cliente y se busca en la veterinaria.
            cliente = veterinaria.buscar_cliente(nombre_cliente)
            if cliente:# - Si el cliente existe, se pide el nombre de la mascota y se busca entre las mascotas del cliente.
                nombre_mascota = input("Nombre de la mascota: ")
                mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
                if mascota:
                    print(f"\nHistorial de servicios de {nombre_mascota}:")
                    mascota.historial.mostrar_historial()# - Si se encuentra la mascota, se imprime su historial de servicios llamando a `mostrar_historial()`.
                else:
                    print("Error: Mascota no encontrada.")# - Si no se encuentra la mascota o el cliente, se muestra un mensaje de error correspondiente.
            else:
                print("Error: Cliente no encontrado.")

        elif opcion == "5":# Si el usuario elige la opción 5:


# Finalmente, si este archivo se ejecuta directamente:
# - Se llama a la función 'menu()' para iniciar el sistema.

            print("Saliendo del sistema...")# - Se imprime un mensaje indicando que se saldrá del sistema.

            break# - Se usa 'break' para salir del bucle y finalizar el programa.

        else:
            print("Opción no válida. Intente de nuevo.")# Si el usuario ingresa una opción no válida:
            # - Se muestra un mensaje indicando que la opción no es válida.



if __name__ == "__main__":# Finalmente, si este archivo se ejecuta directamente:
# - Se llama a la función 'menu()' para iniciar el sistema.

    menu()

