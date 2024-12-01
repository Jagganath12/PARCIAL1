import os

archivo_fna = "C:/Users/Samuel/PycharmProjects/pythonProject1/Bsubtilis_CDS.fna"

# Verificar si el archivo existe
if os.path.isfile(archivo_fna):
    print("El archivo existe y se puede abrir.")
else:
    print("El archivo no existe en la ruta especificada.")