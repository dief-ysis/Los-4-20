import csv 

num_pisos = 5
num_habitaciones_pisos = 8
precios_pisos = {1 : 3000, 2 : 3000, 3 : 3000, 4 : 60000, 5 : 100000}

habitaciones = {}

for piso in range(1, num_pisos + 1):
    for num_hab in range(1, num_habitaciones_pisos + 1):
        numero_habitacion = piso * 10 + num_hab
        precio_habitacion = precios_pisos[piso]
        habitaciones[numero_habitacion] = {
            'Numero': numero_habitacion,
            'Piso': piso,
            'Precio': precio_habitacion,
            'Reservada': False,
            'Nombre': None,
            'Apellido': None,
            'RUT': None,
            'Fecha de ingreso': None,
            'Fecha de salida': None
        }

def reservar_habitacion(codigo_habitacion, nombre, apellido, rut, fecha_ingreso, fecha_salida):
    habitacion = habitaciones.get(codigo_habitacion)
    if habitacion and not habitacion['Reservada']:
        habitacion['Reservada'] = True
        habitacion['Nombre'] = nombre
        habitacion['Apellido'] = apellido
        habitacion['RUT'] = rut
        habitacion['Fecha de ingreso'] = fecha_ingreso
        habitacion['Fecha de salida'] = fecha_salida
        return True
    else:
        return False
    
def buscar_habitacion(codigo_habitacion):
    habitacion = habitaciones.get(codigo_habitacion)
    if habitacion:
        return habitacion
    else:
        return None

def ver_estado():
    return list(habitaciones.values())

def ventas_diarias():
    total_ventas = 0
    for habitacion in habitaciones.values():
        if habitacion['Reservada']:
            total_ventas += habitacion['Precio']
    return total_ventas

def guardar_informacion():
    with open('estado_habitaciones.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Numero', 'Piso', 'Precio', 'Reservada', 'Nombre', 'Apellido', 'RUT', 'Fecha de ingreso', 'Fecha de salida'])
        for habitacion in habitaciones.values():
            writer.writerow([habitacion['Numero'], habitacion['Piso'], habitacion['Precio'], habitacion['Reservada'],
                             habitacion['Nombre'], habitacion['Apellido'], habitacion['RUT'],
                             habitacion['Fecha de ingreso'], habitacion['Fecha de salida']])
    print("Archivo 'estado_habitaciones.csv' creado exitosamente.")

def main():
    while True:
        print("\nBienvenido al sistema de gestión de habitaciones del hotel.")
        print("1. Reservar habitación")
        print("2. Buscar habitación")
        print("3. Ver estado de todas las habitaciones")
        print("4. Calcular ventas diarias")
        print("5. Guardar información en archivo CSV")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                codigo_habitacion = int(input("Ingrese el código de la habitación a reservar: "))
                nombre = input("Ingrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                rut = input("Ingrese su RUT: ")
                fecha_ingreso = input("Ingrese la fecha y hora de ingreso (formato YYYY-MM-DD HH:MM): ")
                fecha_salida = input("Ingrese la fecha y hora de salida (formato YYYY-MM-DD HH:MM): ")

                exito = reservar_habitacion(codigo_habitacion, nombre, apellido, rut, fecha_ingreso, fecha_salida)
                if exito:
                    print(f"Habitación {codigo_habitacion} reservada exitosamente.")
                else:
                    print(f"La habitación {codigo_habitacion} no está disponible para reservar.")
            
            except ValueError:
                print("Error: Ingrese un número de habitación válido.")

        elif opcion == '2':
            try:
                codigo_habitacion = int(input("Ingrese el código de la habitación a buscar: "))
                informacion = buscar_habitacion(codigo_habitacion)
                if informacion:
                    print("\nInformación de la habitación encontrada:")
                    for key, value in informacion.items():
                        print(f"{key}: {value}")
                else:
                    print(f"No se encontró la habitación con código {codigo_habitacion}.")
            
            except ValueError:
                print("Error: Ingrese un número de habitación válido.")

        elif opcion == '3':
            print("\nEstado actual de todas las habitaciones:")
            estados = ver_estado()
            for estado in estados:
                print("\nHabitación:")
                for key, value in estado.items():
                    print(f"{key}: {value}")

        elif opcion == '4':
            ventas = ventas_diarias()
            print(f"\nTotal de ventas del día: ${ventas}")

        elif opcion == '5':
            guardar_informacion()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()
