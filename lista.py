
import csv
def calcular_nota_presentacion(p1, p2, p3):
    return 0.3 * p1 + 0.35 * p2 + 0.35 * p3


def calcular_porcentaje_asistencia(asistencias, total_clases):
    return (asistencias / total_clases) * 100

def verificar_aprobacion_por_asistencia(asistencias, total_clases):
    porcentaje_asistencia = calcular_porcentaje_asistencia(asistencias, total_clases)
    if porcentaje_asistencia >= 65:
        return "Aprobado"
    else:
        return "Reprobado por inasistencia (RI)"
    
def actualizar_archivo_notas(nombre_archivo, nota_presentacion, resultado_asistencia):
    try:
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"Nota de presentación: {nota_presentacion:.2f}\n")
            archivo.write(f"Resultado de asistencia: {resultado_asistencia}\n")
        print("Archivo actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar el archivo: {e}")




guardar_asistencia=[]
buscar_asistencia=[]
notas=[]
while True:
    with open('lista.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            print(fila)
        opcion = int(input(" 1)guardar asistencia  \n 2)buscar asistencia \n 3) calcular notas  \n 4) Salir ").lower())
        if opcion == 1:
            nombre = input("Nombre del estudiante: ")   
            

            guardar_asistencia(nombre)
        elif opcion == 2:
            nombre = input("Nombre del estudiante: ")
            fecha = input("Fecha (DD-MM-YY): ")
            buscar_asistencia(nombre, fecha)

        elif opcion==3:
        
            notas=int(input(""))
            calcular_nota_presentacion()

        elif opcion == 4:
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.")
