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