import pygame
import sys
import random
import time

# Configuración inicial
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Configuración de estrellas
num_stars = 500
stars = [
    (
        random.randint(0, 800),  # Coordenada X
        random.randint(0, 800),  # Coordenada Y
        random.randint(1, 3),    # Tamaño
        random.randint(100, 255)  # Brillo
    )
    for _ in range(num_stars)
]

def actualizar_estrellas():
    """Actualiza las estrellas para animar el cielo."""
    for i, (x, y, size, brightness) in enumerate(stars):
        y += 1  # Mueve la estrella hacia abajo
        if y > 800:  # Si la estrella sale de la pantalla
            x = random.randint(0, 800)  # Nueva posición X
            y = 0  # Reinicia en la parte superior
        brightness = random.randint(100, 255)  # Cambia el brillo aleatoriamente
        stars[i] = (x, y, size, brightness)

def dibujar_estrellas():
    """Dibuja las estrellas en la pantalla."""
    for x, y, size, brightness in stars:
        color = (brightness, brightness, brightness)
        pygame.draw.circle(screen, color, (x, y), size)

def animar_cielo_estrellado():
    """Dibuja el cielo estrellado continuamente."""
    actualizar_estrellas()
    dibujar_estrellas()

def animate_name(name1, combo_value, width=800, height=800):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    # Colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Fuente
    font_path = "fonts/Ballet.ttf"
    font = pygame.font.Font(font_path, 74)
    combo_font = pygame.font.Font(font_path, 66)

    # Variables para la animación
    fixed_name_text = ""  # Para el nombre fijo
    combo_text = ""  # Para el texto del ComboBox
    name_text = ""  # Para el texto del name1
    write_speed = 300  # Velocidad de escritura (en milisegundos)
    last_update_time = pygame.time.get_ticks()

    # Cambiar el ícono de la ventana
    icon_path = "logo/legend.png"
    try:
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
    except FileNotFoundError:
        print(f"No se encontró el ícono en {icon_path}. Se usará el predeterminado.")

    # Cargar el archivo MIDI desde la carpeta Song
    #pygame.mixer.music.load("Song/Decade.mid")
    #pygame.mixer.music.play(-1)  # -1 para que se repita indefinidamente

    # Texto fijo para el nombre
    fixed_name = "Happy New Year"  # Este es el texto fijo que se va a mostrar

    # Diccionario de imágenes basado en el valor del ComboBox
    images = {
        "Michi Town": "img/Gato.png",  # Ruta de la imagen para "Best Wishes"
        "Culto de Paquito": "img/Pacolio.png",  # Ruta de la imagen para "Success"
        "Love": "img/Love.png",  # Ruta de la imagen para "Love"
    }

    # Intentar cargar la imagen correspondiente según el valor del ComboBox
    def cargar_imagen(combo_value):
        try:
            return pygame.image.load(images[combo_value])
        except KeyError:
            return None  # Si no se encuentra la clave, no se carga ninguna imagen

    # Cargar la imagen inicial
    image = cargar_imagen(combo_value)

    # Bucle principal
    state = "fixed_name"  # Estado inicial
    image_shown = False  # Bandera para saber si mostrar la imagen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Actualiza tiempo y texto
        current_time = pygame.time.get_ticks()
        if state == "fixed_name":
            if current_time - last_update_time >= write_speed and len(fixed_name_text) < len(fixed_name):
                fixed_name_text += fixed_name[len(fixed_name_text)]
                last_update_time = current_time
            if len(fixed_name_text) == len(fixed_name):
                state = "combo"  # Cambia al ComboBox

        elif state == "combo":
            if len(combo_text) < len(combo_value):
                if current_time - last_update_time >= write_speed:
                    combo_text += combo_value[len(combo_text)]
                    last_update_time = current_time
            if len(combo_text) == len(combo_value):
                state = "name"  # Cambia al name1

        elif state == "name":
            if len(name_text) < len(name1):
                if current_time - last_update_time >= write_speed:
                    name_text += name1[len(name_text)]
                    last_update_time = current_time
            if len(name_text) == len(name1):
                image_shown = True  # Muestra la imagen después de que termine la animación

        # Dibujar fondo y estrellas
        screen.fill(BLACK)
        animar_cielo_estrellado()

        # Mostrar el nombre fijo animado
        fixed_name_surface = font.render(fixed_name_text, True, WHITE)
        fixed_name_rect = fixed_name_surface.get_rect(center=(800 // 2, 800 // 5))  # Ajusté más el espacio arriba
        screen.blit(fixed_name_surface, fixed_name_rect)

        # Mostrar el valor del ComboBox animado
        if state == "combo" or state == "name":
            combo_text_surface = combo_font.render(combo_text, True, WHITE)
            combo_text_rect = combo_text_surface.get_rect(center=(800 // 2, 800 // 2.5))  # Más espacio
            screen.blit(combo_text_surface, combo_text_rect)

        # Mostrar el name1 animado
        if state == "name":
            name_text_surface = font.render(name_text, True, WHITE)
            name_text_rect = name_text_surface.get_rect(center=(800 // 2, 800 // 1.75))  # Más espacio
            screen.blit(name_text_surface, name_text_rect)

        # Mostrar la imagen solo después de la animación
        if image_shown and image:
            image_rect = image.get_rect(center=(800 // 2, 800 // 1.25))  # Colocar la imagen más abajo
            screen.blit(image, image_rect)

        pygame.display.flip()
        clock.tick(60)

# Ejecuta la animación
#animate_name("Name", "Best Wishes")
