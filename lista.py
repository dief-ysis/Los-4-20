import csv
with open('lista.csv', 'r', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow([fecha_actual, nombre, asistencia])
    print(f"Asistencia de {nombre} guardada para el {fecha_actual}.")
