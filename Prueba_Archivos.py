import os

# Actualiza la ruta del archivo con la extensión correcta
archivo_fna = "C:/Users/Samuel/PycharmProjects/pythonProject1/Bsubtilis_CDS.fna.txt"

# Verificar si el archivo existe
if os.path.isfile(archivo_fna):
    print("El archivo existe y se puede abrir.")
else:
    print("El archivo no existe en la ruta especificada.")

# Abrir el archivo y leer su contenido
try:
    with open(archivo_fna, 'r') as file:
        contenido = file.read()  # Lee todo el contenido del archivo
        print(contenido)  # Muestra el contenido del archivo
except Exception as e:
    print(f"Error al abrir el archivo: {e}")
