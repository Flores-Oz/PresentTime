import pygame
import sys

# Animación de escribir el nombre y el ComboBox
def animate_name(name1, combo_value):
    pygame.init()

    # Colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Fuente
    font = pygame.font.SysFont("Arial", 74)
    combo_font = pygame.font.SysFont("Arial", 36)  # Fuente para el ComboBox

    # Variables para la animación
    fixed_name_text = ""  # Para el nombre fijo
    combo_text = ""  # Para el texto del ComboBox
    name_text = ""  # Para el texto del name1
    write_speed = 300  # Velocidad de escritura (en milisegundos)
    last_update_time = pygame.time.get_ticks()

    # Tamaños de ventana
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Happy New Year")

    # Texto fijo para el nombre
    fixed_name = "Happy New Year"  # Este es el texto fijo que se va a mostrar

    # Bucle principal
    clock = pygame.time.Clock()

    # Estado para saber qué texto se está escribiendo
    state = "fixed_name"  # Primero se escribirá el nombre fijo

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Animación de escribir el nombre fijo
        current_time = pygame.time.get_ticks()
        if state == "fixed_name":
            if current_time - last_update_time >= write_speed and len(fixed_name_text) < len(fixed_name):
                fixed_name_text += fixed_name[len(fixed_name_text)]
                last_update_time = current_time
            if len(fixed_name_text) == len(fixed_name):
                state = "combo"  # Una vez que termine de escribir el nombre fijo, pasa al ComboBox

        # Animación del combo_value
        elif state == "combo":
            if len(combo_text) < len(combo_value):
                if current_time - last_update_time >= write_speed:
                    combo_text += combo_value[len(combo_text)]
                    last_update_time = current_time
            if len(combo_text) == len(combo_value):
                state = "name"  # Una vez que termine de escribir el combo_value, pasa al nombre ingresado

        # Animación del name1
        elif state == "name":
            if len(name_text) < len(name1):  # Animación del texto de name1
                if current_time - last_update_time >= write_speed:
                    name_text += name1[len(name_text)]
                    last_update_time = current_time

        # Dibujar pantalla
        screen.fill(BLACK)

        # Mostrar el nombre fijo animado
        fixed_name_surface = font.render(fixed_name_text, True, WHITE)
        fixed_name_rect = fixed_name_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(fixed_name_surface, fixed_name_rect)

        # Mostrar el valor del ComboBox animado
        if state == "combo" or state == "name":
            combo_text_surface = combo_font.render(combo_text, True, WHITE)
            combo_text_rect = combo_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
            screen.blit(combo_text_surface, combo_text_rect)

        # Mostrar el name1 animado
        if state == "name":
            name_text_surface = font.render(name_text, True, WHITE)
            name_text_rect = name_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))
            screen.blit(name_text_surface, name_text_rect)

        pygame.display.flip()
        clock.tick(60)
