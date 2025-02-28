#Ejercicio Filtrar y mover imagenes por fecha de creacion

'''Explorar la carpeta de origen:
Usaremos os.listdir() para listar los archivos en la carpeta de origen.

Filtrar imágenes:
Verificaremos que los archivos sean imágenes .jpg o .png.

Extraer la fecha de creación:
Usaremos os.stat() para obtener la fecha de creación de los archivos.

Crear subcarpetas por año:
Si no existe una carpeta con el nombre del año de creación, la crearemos con os.mkdir().

Mover los archivos:
Usaremos shutil.move() para mover las imágenes a su carpeta correspondiente.'''

import os
import shutil
import datetime

# Definir rutas de origen y destino
ruta_origen = r"C:/Users/sam/Desktop/J"
ruta_destino = r"C:/Users/sam/Desktop/images"

# Listar todos los archivos en la carpeta de origen
archivos = os.listdir(ruta_origen)
imagenes = [archivo for archivo in archivos if archivo.endswith('.jpg') or archivo.endswith('png') ]

# Iterar sobre las imagenes encontradas
for imagen in imagenes:
    # Ruta completa del archivo
    ruta_imagen = os.path.join(ruta_origen, imagen)

    # Obetener la fecha de creación (timestamp)
    info_archivo = os.stat(ruta_imagen)

    # Extrae el año de la fecha de creacion, como me está devolviendo la fecha en formato
    # Unix,voy a convertir el timestamp en una fecha legible

    #Lo obtenemos
    timestamp = info_archivo.st_birthtime

    #Convertimos a objeto datatime
    fecha_creacion = datetime.datetime.fromtimestamp(timestamp)
    anio_creacion = str(fecha_creacion).split()[0].split('-')[0]
    
    # Crear una carpeta para ese año si no existe
    carpeta_destino = os.path.join(ruta_destino, anio_creacion)
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Mover la imagen a la carpeta correspondiente
    shutil.move(ruta_imagen, os.path.join(carpeta_destino, imagen))

print('Proceso completado.')

