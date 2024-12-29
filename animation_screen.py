# animation_screen.py
import pygame
import sys

# Animación de escribir el nombre y el ComboBox
def animate_name(name, combo_value):
    pygame.init()

    # Colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Fuente
    font = pygame.font.SysFont("Arial", 74)
    combo_font = pygame.font.SysFont("Arial", 36)  # Fuente para el ComboBox

    # Variables para la animación
    current_text = ""
    combo_text = ""
    write_speed = 300  # Velocidad de escritura (en milisegundos)
    last_update_time = pygame.time.get_ticks()

    # Tamaños de ventana
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Animación de Escribir Nombre y ComboBox")

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

        # Animación de escribir el combo_value
        if len(combo_text) < len(combo_value):
            if current_time - last_update_time >= write_speed:
                combo_text += combo_value[len(combo_text)]
                last_update_time = current_time

        # Dibujar pantalla
        screen.fill(BLACK)

        # Mostrar el nombre animado
        text_surface = font.render(current_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))  # Ajusté la posición en el eje Y
        screen.blit(text_surface, text_rect)

        # Mostrar el valor del ComboBox animado
        combo_text_surface = combo_font.render(combo_text, True, WHITE)  # Eliminé el prefijo "Selección: "
        combo_text_rect = combo_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))  # Ajusté la posición en el eje Y
        screen.blit(combo_text_surface, combo_text_rect)

        pygame.display.flip()
        clock.tick(60)
