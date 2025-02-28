#Ejericio obtencion de extensiones. Ordenacion en subcarpetas por tipo.

import os
import utilities
from pathlib import Path

# Ruta de trabajo
ruta_origen = Path("C:/Users/sam/Desktop/J")

# Listar las extensiones
archivos = [archivo.name for archivo in ruta_origen.iterdir() if archivo.is_file()]
print(archivos)
extensiones = {Path(archivo).suffix.lower() for archivo in archivos if Path(archivo).suffix}
print(extensiones)

# Iterar el conjunto y obtener los nuevos directorios.
for extension in extensiones:
    directorio_extension = Path.joinpath(ruta_origen, extension)
    if not directorio_extension.exists():
        utilities.crear_directorio(directorio_extension)
for archivo in archivos:
    tipo = os.path.splitext(archivo)[1].lower()
    if not tipo:
        continue
    ruta_document = os.path.join(ruta_origen, archivo)
    ruta_destino = os.path.join(ruta_origen, tipo)
    utilities.mover_archivo(ruta_document, ruta_destino)
print(f"Se han ordenado los archivos")
   

