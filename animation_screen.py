# animation_screen.py
import pygame
import sys

# Animación de escribir el nombre
def animate_name(name):
    pygame.init()

    # Colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Fuente
    font = pygame.font.SysFont("Arial", 74)

    # Variables para la animación
    current_text = ""
    write_speed = 300  # Velocidad de escritura (en milisegundos)
    last_update_time = pygame.time.get_ticks()

    # Tamaños de ventana
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Animación de Escribir Nombre")

    # Bucle principal
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Animación de escribir nombre
        current_time = pygame.time.get_ticks()
        if current_time - last_update_time >= write_speed and len(current_text) < len(name):
            current_text += name[len(current_text)]
            last_update_time = current_time

        # Dibujar pantalla
        screen.fill(BLACK)
        text_surface = font.render(current_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)
