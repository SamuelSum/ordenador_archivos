#Automatizacion de tareas - Copiar archivos según condiciones
# Ejercicio: Copiar solo los .txt de un directorio origen en otro destino.

#He creado los directorios "documentos_papeleria" y "backup"
#Vamos a extraer los .txt y hacer una copia de seguridad en backup

import os
import shutil

# Definir las rutas de origen y destino
origen = r'C:/Users/sam/Desktop/documentos_papeleria'
destino = r'C:/Users/sam/Desktop/backup'

# Verificar si el directorio de destino existe, si no, crear uno
if not os.path.exists(destino):
        os.makedirs(destino)

# Iterar sobre los archivos en el directorio de origen
for archivo in os.listdir(origen):
        ruta_origen =  os.path.join(origen, archivo)
        ruta_destino = os.path.join(destino, archivo)

        # Verifixar si es un archibo .txt
        if os.path.isfile(ruta_origen) and archivo.endswith('.txt'):
                # Copiar el .txt al destino
                shutil.copy(ruta_origen, ruta_destino)
                print(f"Archivo copiado: {archivo}")
                print(ruta_destino)


