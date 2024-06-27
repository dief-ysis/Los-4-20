import csv
from datetime import date

def guardar_asistencia(nombre, asistencia):
    fecha_actual = date.today().strftime('%d-%m-%y')
    with open('asistencia.csv', 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow([fecha_actual, nombre, asistencia])
    print(f"Asistencia de {nombre} guardada para el {fecha_actual}.")

def buscar_asistencia(nombre, fecha):
    try:
        with open('asistencia.csv', 'r') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for row in reader:
                if row[0] == fecha and row[1] == nombre:
                    print(f"{nombre} estuvo {'presente' if row[2] == 'True' else 'ausente'} el {fecha}.")
                    return
            print(f"No se encontro asistencia para {nombre} el {fecha}.")
    except FileNotFoundError:
        print("No hay registros de asistencia todavia.")


while True:
    opcion = input("¿Deseas guardar asistencia (G) o buscar asistencia (B)? o salir (salir) \n ").lower()
    if opcion == 'g':
        nombre = input("Nombre del estudiante: ")
        asistencia = input("¿Estuvo presente? (Si/No): ").lower() == 'si'
        guardar_asistencia(nombre, asistencia)
    elif opcion == 'b':
        nombre = input("Nombre del estudiante: ")
        fecha = input("Fecha (DD-MM-YY): ")
        buscar_asistencia(nombre, fecha)
    elif opcion == "salir":
        break
    else:
        print("Opcion no valida. Intentalo de nuevo.")


































        ###############################################

def calcular_nota_presentacion(p1, p2, p3):
    nota_presentacion = 0.3 * p1 + 0.35 * p2 + 0.35 * p3
    return nota_presentacion

# Ejemplo de uso:
p1 = 7.5
p2 = 8.0
p3 = 6.5
nota_final = calcular_nota_presentacion(p1, p2, p3)
print(f"Nota de presentación: {nota_final:.2f}")







def calcular_porcentaje_asistencia(asistencias):
total_clases = len(asistencias)
asistencias_totales = sum(asistencias)
porcentaje_asistencia = (asistencias_totales / total_clases) * 100
return porcentaje_asistencia

def evaluar_asistencia(asistencias):
    porcentaje_minimo_aprobacion = 75
    porcentaje_actual = calcular_porcentaje_asistencia(asistencias)
    if porcentaje_actual >= porcentaje_minimo_aprobacion:
        return "Aprueba"
    else:
        return "Reprueba por inasistencia"

# Ejemplo de uso:
asistencias_alumno = [True, True, False, True, True, False]
resultado_asistencia = evaluar_asistencia(asistencias_alumno)
print(f"Resultado de asistencia: {resultado_asistencia}")