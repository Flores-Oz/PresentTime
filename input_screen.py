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
    combo_font = pygame.font.Font(font_path, 20)  # Puedes ajustar el tamaño según lo necesites
    combo_font1= pygame.font.Font(font_path, 18)  
    # Variables de entrada
    input_text = ""
    active_screen = "input"  # Cambiará entre 'input' y 'animation'
    
    # Variables para el ComboBox
    combo_active = False  # Determina si el combo está abierto
    combo_options = ["Michi Town", "Culto de Paquito",]
    combo_selected = "Selecciona una opción"
    
    # Tamaños de ventana
    INPUT_WIDTH, INPUT_HEIGHT = 400, 300

    # Configuración de la ventana inicial
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
    pygame.mixer.music.play(-1)  # -1 para que se repita indefinidamente

    # Rectángulos para entrada de texto y ComboBox
    #input_rect = pygame.Rect(INPUT_WIDTH // 4, INPUT_HEIGHT // 3, INPUT_WIDTH // 2, 50)  # Campo para el nombre
    input_rect = pygame.Rect((INPUT_WIDTH // 2 - INPUT_WIDTH // 2 // 2, INPUT_HEIGHT // 3 - 25),(INPUT_WIDTH // 2, 50))
    #combo_rect = pygame.Rect(INPUT_WIDTH // 4, INPUT_HEIGHT // 2 + 10, INPUT_WIDTH // 1.5, 50)  # ComboBox debajo del nombre
    combo_rect = pygame.Rect((INPUT_WIDTH // 2 - INPUT_WIDTH // 1.5 // 2, INPUT_HEIGHT // 2-25),(INPUT_WIDTH // 1.5, 50))

    combo_rects = []  # Listado de rectángulos de opciones para el ComboBox
    for i, option in enumerate(combo_options):
        option_rect = pygame.Rect(combo_rect.x, combo_rect.y + 50 + (i * 50), combo_rect.width, 50)
        combo_rects.append(option_rect)

    # Bucle principal
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
                            return input_text, combo_selected
                    elif event.key == pygame.K_BACKSPACE:  # Borra el último carácter
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode  # Agrega la letra ingresada

            if event.type == pygame.MOUSEBUTTONDOWN:
                if combo_rect.collidepoint(event.pos):  # Si hace clic en el ComboBox
                    combo_active = not combo_active  # Cambia el estado del ComboBox

                # Si el ComboBox está abierto y se hace clic en una opción
                if combo_active:
                    for i, rect in enumerate(combo_rects):
                        if rect.collidepoint(event.pos):
                            combo_selected = combo_options[i]
                            combo_active = False

        # Pantalla de entrada de nombre
        screen.fill(BLACK)

        # Mensaje
        message = "¿Cual es tu Nombre?:"
        message_surface = font.render(message, True, WHITE)
        message_rect = message_surface.get_rect(center=(INPUT_WIDTH // 2, INPUT_HEIGHT // 4 - 20))
        screen.blit(message_surface, message_rect)

        # Cuadro de entrada para el nombre
        pygame.draw.rect(screen, GRAY, input_rect, border_radius=10)
        pygame.draw.rect(screen, BLUE, input_rect, 2, border_radius=10)

        # Texto ingresado
        input_surface = font.render(input_text, True, WHITE)
        screen.blit(input_surface, (input_rect.x + 10, input_rect.y + 10))

        # Cuadro del ComboBox
        pygame.draw.rect(screen, GRAY, combo_rect, border_radius=10)
        pygame.draw.rect(screen, BLUE, combo_rect, 2, border_radius=10)

        # Texto del ComboBox
        combo_surface = combo_font1.render(combo_selected, True, WHITE)
        screen.blit(combo_surface, (combo_rect.x + 10, combo_rect.y + 10))

        # Si el ComboBox está abierto, mostrar las opciones
        if combo_active:
            for i, option in enumerate(combo_options):
                option_rect = combo_rects[i]
                pygame.draw.rect(screen, GRAY, option_rect, border_radius=10)
                pygame.draw.rect(screen, BLUE, option_rect, 2, border_radius=10)
                option_surface = combo_font.render(option, True, WHITE)
                screen.blit(option_surface, (option_rect.x + 10, option_rect.y + 10))

        pygame.display.flip()
        clock.tick(60)
