def main():
    nombre_archivo = 'lista.csv'
    estudiantes = leer_archivo_estudiantes(nombre_archivo)
    actualizar_archivo(estudiantes)
    promedio_total = calcular_promedio_ponderado_total(estudiantes)
    print(f"Promedio ponderado total del curso: {promedio_total}")
    print("Archivo 'registro_estudiantes_actualizado.txt' actualizado correctamente.")
if __name__ == "__main__":
    main()