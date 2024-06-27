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