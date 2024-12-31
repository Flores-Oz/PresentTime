import sys
from input_screen import get_name
from animation_screen import animate_name
from animation_sky import animacion_sky  # Importa la nueva función de cielo
import subprocess
import os

# Función para obtener la ruta correcta de los recursos
def resource_path(relative_path):
    """Obtiene la ruta correcta al recurso en diferentes sistemas operativos y entornos."""
    try:
        # Para aplicaciones empaquetadas, obtener la ruta del recurso dentro del paquete
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        # Para un entorno normal, usar la ruta relativa
        return os.path.join(os.path.dirname(__file__), relative_path)
    except Exception as e:
        print(f"Error al obtener la ruta del recurso: {e}")
        return relative_path

# Función para ejecutar el script
def ejecutar_script(script_name):
    """Ejecuta el script especificado cuando se hace clic en el segundo botón."""
    script_path = resource_path(script_name)  # Obtener la ruta correcta del script
    try:
        # Ejecutar el script .py (también funcionará si es empaquetado en .exe)
        subprocess.Popen([sys.executable, script_path])  # Ejecutar el script usando el intérprete de Python
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")

# Obtener el nombre desde la pantalla de entrada
name, combo_value = get_name()

# Primero, ejecutamos la animación del cielo de estrellas
animacion_sky()  # Llamamos a la animación del cielo

# Iniciar la animación con el nombre ingresado
animate_name(name, combo_value)

# Cuando el segundo botón es presionado, ejecuta el script whatsyourfire.py
ejecutar_script("whatsyourfire.py")
