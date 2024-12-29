# input_screen.py
import pygame
import sys

# Función para obtener el nombre desde la pantalla de entrada
def get_name():
    pygame.init()
    clock = pygame.time.Clock()
    # Colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    BLUE = (0, 120, 215)

    # Fuente
    font_path = "fonts/RubikViny.ttf"  
    font = pygame.font.Font(font_path, 26)

    # Variables de entrada
    input_text = ""
    active_screen = "input"  # Cambiará entre 'input' y 'animation'

    # Tamaños de ventana
    INPUT_WIDTH, INPUT_HEIGHT = 400, 200

    # Configuración de la ventana inicial pequeña
    screen = pygame.display.set_mode((INPUT_WIDTH, INPUT_HEIGHT))
    pygame.display.set_caption("Legend")
    
    # Cambiar el ícono de la ventana
    icon_path = "logo/legend.png"  # Cambia esta ruta por tu archivo .ico
    try:
          icon = pygame.image.load(icon_path)
          pygame.display.set_icon(icon)
    except FileNotFoundError:
          print(f"No se encontró el ícono en {icon_path}. Se usará el predeterminado.")

    # Cargar el archivo MIDI desde la carpeta Song
    pygame.mixer.music.load("Song/name.mp3")
    # Reproducir el archivo
    pygame.mixer.music.play(-1) 

    # Bucle principal
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()  
                pygame.quit()
                sys.exit()
            if active_screen == "input":  # Manejo de eventos para la pantalla de entrada
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Si presiona Enter, retorna el nombre
                        if input_text.strip():
                            return input_text
                    elif event.key == pygame.K_BACKSPACE:  # Borra el último carácter
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode  # Agrega la letra ingresada

        # Pantalla de entrada de nombre
        if active_screen == "input":
            screen.fill(BLACK)

            # Mensaje
            message = "¿Cual es tu Nombre?:"
            message_surface = font.render(message, True, WHITE)
            message_rect = message_surface.get_rect(center=(INPUT_WIDTH // 2, INPUT_HEIGHT // 3))
            screen.blit(message_surface, message_rect)

            # Cuadro de entrada
            input_rect = pygame.Rect(INPUT_WIDTH // 4, INPUT_HEIGHT // 2, INPUT_WIDTH // 2, 50)
            pygame.draw.rect(screen, GRAY, input_rect, border_radius=10)
            pygame.draw.rect(screen, BLUE, input_rect, 2, border_radius=10)

            # Texto ingresado
            input_surface = font.render(input_text, True, WHITE)
            screen.blit(input_surface, (input_rect.x + 10, input_rect.y + 10))

        pygame.display.flip()
        clock.tick(60)
