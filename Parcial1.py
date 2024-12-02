import os
import re
import xlsxwriter  # Para gaurdar el archivo en excel

# Función para verificar si el archivo existe y es accesible
def verificar_archivo(archivo_fna):
    if os.path.isfile(archivo_fna):
        print("El archivo existe y se puede abrir.")
        return True
    else:
        print("El archivo no existe en la ruta especificada.")
        return False

# Función para leer el archivo .fna.txt y extraer las secuencias
def leer_secuencias(archivo_fna):
    secuencias = []
    with open(archivo_fna, 'r') as file:
        secuencia = ""
        for line in file:
            line = line.strip()
            if not line.startswith(">"):
                secuencia += line  # Agregar la secuencia
            else:
                if secuencia:
                    secuencias.append(secuencia)
                    secuencia = ""  # Reiniciar
        if secuencia:
            secuencias.append(secuencia)  # Agregar la última secuencia
    return secuencias

# Función para buscar motivos comunes en las secuencias de ADN
def buscar_motivos(secuencias, motivo):
    resultados = []
    for seq in secuencias:
        posiciones = [m.start() for m in re.finditer(motivo, seq)]
        if posiciones:  # Si se encuentran posiciones para el motivo
            resultados.append({
                'secuencia': seq,
                'motivo': motivo,
                'posiciones': posiciones
            })
    return resultados

# Función para guardar los resultados en un archivo Excel
def guardar_resultados(resultados, archivo_salida):
    workbook = xlsxwriter.Workbook(archivo_salida)
    worksheet = workbook.add_worksheet()

    # Escribir encabezados
    worksheet.write("A1", "Secuencia")
    worksheet.write("B1", "Motivo")
    worksheet.write("C1", "Posiciones")

    row = 1
    for resultado in resultados:
        worksheet.write(row, 0, resultado['secuencia'])
        worksheet.write(row, 1, resultado['motivo'])
        worksheet.write(row, 2, str(resultado['posiciones']))
        row += 1

    workbook.close()
    print(f"Resultados guardados en {archivo_salida}")

# Función principal para procesar las secuencias
def procesar_secuencias(archivo_fna, motivo, archivo_salida):
    if verificar_archivo(archivo_fna):
        secuencias = leer_secuencias(archivo_fna)
        resultados = buscar_motivos(secuencias, motivo)
        if resultados:
            guardar_resultados(resultados, archivo_salida)
        else:
            print("No se encontraron motivos en las secuencias.")
    else:
        print("No se puede procesar el archivo debido a que no existe o no es accesible.")

# Definir las rutas de entrada y salida
archivo_fna = "C:/Users/Samuel/PycharmProjects/PARCIAL1/Bsubtilis_CDS.fna.txt"  # Ruta del archivo .fna.txt(Pon tu ruta)
motivo = "TATAAA"  # Motivo de ejemplo (puedes cambiarlo a lo que busques)
motivo = motivo.upper()
archivo_salida = "resultados_motivos.xlsx"  # Ruta de salida para el archivo Excel

# Ejecutar la función principal
procesar_secuencias(archivo_fna, motivo, archivo_salida)
