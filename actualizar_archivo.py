def actualizar_archivo(estudiantes):
    with open('registro_estudiantes_actualizado.txt', 'w') as archivo:
        for estudiante in estudiantes:
            nota_presentacion = calcular_nota_presentacion(estudiante['p1'], estudiante['p2'], estudiante['p3'])
            estado_ri = verificar_asistencia(estudiante['asistencias'])
            archivo.write(f"{estudiante['nombre']}: NP={nota_presentacion}, RI={estado_ri}\n")