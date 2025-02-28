# Ejercicio ordenar documentos segun año y mes.

import os
from datetime import datetime
from utilities import crear_directorio, mover_archivo

# Especificar las rutas de origen y destino.
ruta_origen = r'C:/Users/sam/Desktop/J'
ruta_destino = r'C:/Users/sam/Desktop/documents'

# Listar los archivos del origen.
archivos = os.listdir(ruta_origen)
documents = [archivo for archivo in archivos if archivo.endswith('.txt') or archivo.endswith('.pdf')]

# Iterar sobre los documentos encontrados.
for document in documents:
    ruta_document = os.path.join(ruta_origen, document)
    info_document = os.stat(ruta_document)
    fecha_creacion = datetime.fromtimestamp(info_document.st_birthtime)
    año, mes = fecha_creacion.strftime("%Y-%m").split('-')
    
    # Crear una carpeta del año para los documentos.
    directorio_año = os.path.join(ruta_destino, año)
    crear_directorio(directorio_año)
                
    # Ahora una para los meses dentro de los años.
    directorio_mes = os.path.join(directorio_año, mes)
    crear_directorio(directorio_mes)

    #Mover el documento a la carpeta mes correspondiente.
    mover_archivo(ruta_document, directorio_mes)


# Sobre los tipo .txt y .pdf, extraer fecha creacion, mover a carpeta correspondiente,si esta no existe crearla.