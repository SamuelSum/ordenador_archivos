import os
import ctypes

def es_administrador():
    try:
        # Verifica si el script está corriendo con privilegios elevados (administrador)
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

if es_administrador():
    print("El script está corriendo como Administrador.")
else:
    print("El script NO está corriendo como Administrador.")