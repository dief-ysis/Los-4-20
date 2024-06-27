def calcular_nota_presentacion(p1, p2, p3):
    return 0.3 * p1 + 0.35 * p2 + 0.35 * p3

# Ejemplo de uso:
nota_presentacion = calcular_nota_presentacion(7.5, 8.0, 6.5)
print(f"Nota de presentación: {nota_presentacion:.2f}")



def calcular_porcentaje_asistencia(asistencias, total_clases):
    return (asistencias / total_clases) * 100

def verificar_aprobacion_por_asistencia(asistencias, total_clases):
    porcentaje_asistencia = calcular_porcentaje_asistencia(asistencias, total_clases)
    if porcentaje_asistencia >= 80:
        return "Aprobado"
    else:
        return "Reprobado por inasistencia (RI)"

# Ejemplo de uso:
asistencias_alumno = 30
total_clases = 40
resultado_asistencia = verificar_aprobacion_por_asistencia(asistencias_alumno, total_clases)
print(f"Resultado de asistencia: {resultado_asistencia}")



def actualizar_archivo_notas(nombre_archivo, nota_presentacion, resultado_asistencia):
    try:
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"Nota de presentación: {nota_presentacion:.2f}\n")
            archivo.write(f"Resultado de asistencia: {resultado_asistencia}\n")
        print("Archivo actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar el archivo: {e}")

# Ejemplo de uso:
nombre_archivo = "notas.txt"
nota_presentacion_ejemplo = 7.8
resultado_asistencia_ejemplo = "Aprobado"
actualizar_archivo_notas(nombre_archivo, nota_presentacion_ejemplo, resultado_asistencia_ejemplo)




