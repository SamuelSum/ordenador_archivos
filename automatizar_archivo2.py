#Mover y renombrar archivos

import shutil
import os

# Define las rutas de origen y destino
origen = r'C:\Users\sam\Desktop\nominas'
destino = r'C:\Users\sam\Desktop\archivos_movidos'

# Mover el fichero

shutil.move(origen, destino)
print("El archivo ha sido movido.")
