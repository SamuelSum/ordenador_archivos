import os
import shutil
import logging

# Configuracion de logging
logging.basicConfig(
    filename="mover_archivos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

def crear_directorio(*directorios):
   for directorio in directorios:
       if directorio:
            try:
                os.makedirs(directorio, exist_ok=True)
                logging.info(f"Directorio creado: {directorio}")
            except Exception as e:
                logging.error(f"Error al crear directorio: {directorio}")
                
def mover_archivo(ruta_origen, directorio_mes):
    """Mueve un archivo a un destino si es valido."""
    if not os.path.exists(ruta_origen):
        logging.warning(f"El archivo {ruta_origen} no existe, omitiendo...")
        return
    
    try:
        shutil.move(ruta_origen , directorio_mes)
        logging.info(f"Documento movido de {ruta_origen} -> {directorio_mes}")
    except PermissionError:
        logging.error(f"Error: el archivo no se puede mover porque está marcado como solo lectura")
    except Exception as e:
        logging.error(f"Error al mover {e}")

