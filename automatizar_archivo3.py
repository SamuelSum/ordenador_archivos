import os
import shutil

# Definir las rutas de origen y destino

origen = r'C:\Users\sam\Desktop\nominas'
destino = r'C:\Users\sam\Desktop\archivos_movidos'

# Iterar sobre los elementos del directorio de origen

for elemento in os.listdir(origen):
    ruta_origen = os.path.join(origen, elemento)
    ruta_destino = os.path.join(destino, elemento)

    # Verificar si un archivo o un directorio
    if os.path.isdir(ruta_origen):
        #true, es un directorio, moverlo
        shutil.move(ruta_origen, ruta_destino)
    else:
        #false, es un fichero, moverlo
        shutil.move(ruta_origen, ruta_destino)

print("Todo el contenido ha sido movido")
