import csv

def leer_archivo_estudiantes(nombre_archivo):
    estudiantes = []
    
    with open(nombre_archivo, 'r', newline='') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)
        
        for campos in lector_csv:
            estudiante = {
                'nombre': campos[0].strip(),
                'p1': int(campos[1].strip()),
                'p2': int(campos[2].strip()),
                'p3': int(campos[3].strip()),
                'asistencias': list(map(int, campos[4:11]))
            }
            estudiantes.append(estudiante)
    
    return estudiantes

def calcular_nota_presentacion(p1, p2, p3):
    ponderacion_p1 = 0.30
    ponderacion_p2 = 0.35
    ponderacion_p3 = 0.35
    
    nota_presentacion = p1 * ponderacion_p1 + p2 * ponderacion_p2 + p3 * ponderacion_p3
    
    return nota_presentacion

def verificar_asistencia(asistencias):
    total_clases = len(asistencias)
    clases_asistidas = sum(asistencias)
    
    porcentaje_asistencia = (clases_asistidas / total_clases) * 100
    
    if porcentaje_asistencia >= 65:
        return "Aprobado"
    else:
        return "Reprueba por Inasistencia"

def actualizar_archivo(estudiantes):
    with open('registro_estudiantes_actualizado.txt', 'w') as archivo:
        for estudiante in estudiantes:
            nota_presentacion = calcular_nota_presentacion(estudiante['p1'], estudiante['p2'], estudiante['p3'])
            estado_ri = verificar_asistencia(estudiante['asistencias'])
            archivo.write(f"{estudiante['nombre']}: NP={nota_presentacion}, RI={estado_ri}\n")

def calcular_promedio_ponderado_total(estudiantes):
    notas_presentacion = []
    for estudiante in estudiantes:
        nota_presentacion = calcular_nota_presentacion(estudiante['p1'], estudiante['p2'], estudiante['p3'])
        notas_presentacion.append(nota_presentacion)
    if notas_presentacion:
        promedio_ponderado_total = sum(notas_presentacion) / len(notas_presentacion)
    else:
        promedio_ponderado_total = 0
    
    return promedio_ponderado_total

def main():
    nombre_archivo = 'lista.csv'
    estudiantes = leer_archivo_estudiantes(nombre_archivo)
    actualizar_archivo(estudiantes)
    promedio_total = calcular_promedio_ponderado_total(estudiantes)
    print(f"Promedio ponderado total del curso: {promedio_total}")
    print("Archivo 'registro_estudiantes_actualizado.txt' actualizado correctamente.")
if __name__ == "__main__":
    main()