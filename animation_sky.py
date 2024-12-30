import pygame
import random
import sys
import time

# Inicialización
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Configuración de estrellas
num_stars = 500  # Número total de estrellas
stars = [
    (
        random.randint(0, 800),  # Coordenada X
        random.randint(0, 800),  # Coordenada Y
        random.randint(1, 3),    # Tamaño
        random.randint(100, 255)  # Brillo
    )
    for _ in range(num_stars)
]

# Cargar el archivo MIDI desde la carpeta Song
def reproducir_musica():
    try:
        pygame.mixer.music.load("Song/Decade.mid")
        pygame.mixer.music.play(-1)  # Repite indefinidamente
    except pygame.error as e:
        print(f"Error al cargar la música: {e}")
        sys.exit()

# Función para animar el pintado de estrellas con transición suave
def animacion_sky(width=800, height=800):
    pygame.mixer.music.stop()
    reproducir_musica() 
    screen = pygame.display.set_mode((width, height))
    screen.fill((0, 0, 0))  # Fondo negro
    pygame.display.flip()  # Actualiza pantalla inicial

    # Animación del cielo estrellado
    for i, (x, y, size, brightness) in enumerate(stars):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Dibuja la estrella actual
        color = (brightness, brightness, brightness)
        pygame.draw.circle(screen, color, (x, y), size)
        pygame.display.flip()  # Actualiza solo el frame actual
        
        # Retardo entre cada estrella (controla la velocidad de animación)
        time.sleep(0.01)
        
    # Transición suave: fade in o fade out
    fade_surface = pygame.Surface((width, height))
    fade_surface.fill((0, 0, 0))  # Pantalla negra para el fade
    for alpha in range(0, 255, 5):  # Se incrementa la opacidad
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        time.sleep(0.02)

    pygame.display.flip()