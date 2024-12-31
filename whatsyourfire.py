import math
import random
import pygame
import sys
import os
import time  # Necesario para controlar el tiempo

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
    
# Inicialización
pygame.init()
pygame.display.set_caption("Fire")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
particles = [(random.gauss(0, .5), random.uniform(0, 6.28318)) for _ in range(2500)]
colors = [[255, 0, 255], [7, 185, 252], [0, 171, 56], [154, 240, 0], [255, 230, 50], [255, 130, 42], [255, 0, 0]]

# Clase para las explosiones
class Explosion:
    def __init__(self, x, y, radio, color):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.frame = 0
        self.done = False

    def update(self):
        if self.frame >= self.radio:
            self.done = True
            return

        for speed, angle in particles:
            distance = self.frame * speed
            px = self.x + distance * math.cos(angle)
            py = self.y + distance * math.sin(angle)
            if 0 <= px < 800 and 0 <= py < 800:  # Verifica límites
                screen.set_at((int(px), int(py)), self.color)

        self.frame += 1

# Crear explosiones iniciales (6 explosiones)
explosiones = [
    Explosion(random.randint(100, 700), random.randint(100, 700), random.randint(100, 250), random.choice(colors))
    for _ in range(6)
]

# Cambiar el ícono de la ventana
icon_path = resource_path("logo/legend.png")  # Usar resource_path para la ruta del ícono
try:
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
except FileNotFoundError:
        print(f"No se encontró el ícono en {icon_path}. Se usará el predeterminado.")
        
# Cargar el archivo MIDI desde la carpeta Song
pygame.mixer.music.load(resource_path("Song/Explosion.mp3"))  # Usamos la función para obtener la ruta correcta
# Obtener la duración del archivo de audio (en segundos)
audio_duration = pygame.mixer.Sound(resource_path("Song/Explosion.mp3")).get_length()
# Reproducir el archivo
pygame.mixer.music.play(-1)  # -1 para que se repita indefinidamente

# Calcular el tiempo total de animación (duración del audio + 10 segundos)
animation_duration = audio_duration + 21
start_time = time.time()  # Guardar el tiempo de inicio

# Función de desvanecimiento (fade-out) para transición
def fade_out():
    fade_surface = pygame.Surface((800, 800))
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)

# Variables de control de pantalla
screen_state = 'explosion'  # Estado inicial de la pantalla

# Función que simula lo que pasaría en `end.py` con animación
def show_end_screen():
    # Animación para el "Fin del Juego"
    font = pygame.font.SysFont('Arial', 50)
    text = font.render("OPEN YOUR EYES FOR THE NEXT FAIZ", True, (255, 255, 255))
    
    # Desplazamiento de texto desde la parte superior
    text_rect = text.get_rect(center=(400, -50))  # Iniciar fuera de la pantalla
    screen.fill((0, 0, 0))  # Limpiar la pantalla
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Animación de desvanecimiento y desplazamiento
    for i in range(50):
        text_rect.y += 10  # Mover el texto hacia abajo
        text.set_alpha(255 - i * 5)  # Hacer que el texto se desvanezca
        screen.fill((0, 0, 0))  # Limpiar la pantalla
        screen.blit(text, text_rect)  # Dibujar el texto
        pygame.display.flip()
        pygame.time.delay(50)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()  
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    if screen_state == 'explosion':
        # Actualizar y dibujar explosiones
        for explosion in explosiones:
            explosion.update()

        # Revisar si todas las explosiones han terminado y reiniciar
        if all(explosion.done for explosion in explosiones):
            # Aquí ahora generamos siempre 6 explosiones
            explosiones = [
                Explosion(random.randint(100, 700), random.randint(100, 700), random.randint(100, 250), random.choice(colors))
                for _ in range(6)  # Siempre 6 explosiones
            ]

        pygame.display.flip()
        clock.tick(120)  # Velocidad de actualización

        # Comprobar si ha pasado el tiempo de animación total
        elapsed_time = time.time() - start_time
        if elapsed_time >= animation_duration:
            # Detener la música
            pygame.mixer.music.stop()  

            # Realizar la transición (fade-out)
            fade_out()

            # Cambiar al estado de 'end_screen'
            screen_state = 'end_screen'

    elif screen_state == 'end_screen':
        # Aquí se pasa a la lógica de `end.py` con animación
        show_end_screen()
        pygame.quit()
        sys.exit()
