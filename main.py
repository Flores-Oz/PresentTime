import sys
from input_screen import get_name
from animation_screen import animate_name
from animation_sky import animacion_sky  # Importa la nueva función de cielo

# Obtener el nombre desde la pantalla de entrada
name, combo_value = get_name()

# Primero, ejecutamos la animación del cielo de estrellas
animacion_sky()  # Llamamos a la animación del cielo

# Iniciar la animación con el nombre ingresado
animate_name(name, combo_value)
