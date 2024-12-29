# main.py
import sys
from input_screen import get_name
from animation_screen import animate_name

# Obtener el nombre desde la pantalla de entrada
name, combo_value = get_name()

# Iniciar la animación con el nombre ingresado
animate_name(name, combo_value)
