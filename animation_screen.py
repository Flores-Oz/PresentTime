import pygame
import sys
import random
import os
import platform

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
    font_path = resource_path("fonts/Ballet.ttf")  # Usar resource_path para obtener la ruta de la fuente
    font = pygame.font.Font(font_path, 74)
    font1 = pygame.font.SysFont('Arial', 16)
    combo_font = pygame.font.Font(font_path, 66)

    # Variables para la animación
    fixed_name_text = ""  # Para el nombre fijo
    combo_text = ""  # Para el texto del ComboBox
    name_text = ""  # Para el texto del name1
    write_speed = 300  # Velocidad de escritura (en milisegundos)
    last_update_time = pygame.time.get_ticks()

    # Cambiar el ícono de la ventana
    icon_path = resource_path("logo/legend.png")  # Usar resource_path para la ruta del ícono
    try:
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
    except FileNotFoundError:
        print(f"No se encontró el ícono en {icon_path}. Se usará el predeterminado.")

    # Texto fijo para el nombre
    fixed_name = "Happy New Year"  # Este es el texto fijo que se va a mostrar

    # Diccionario de imágenes basado en el valor del ComboBox
    images = {
        "Michi Town": resource_path("img/Gato.png"),  # Usar resource_path para las rutas de las imágenes
        "Culto de Paquito": resource_path("img/Pacolio.png"),
        "Love": resource_path("img/Love.png"),
    }

    # Intentar cargar la imagen correspondiente según el valor del ComboBox
    def cargar_imagen(combo_value):
        try:
            return pygame.image.load(images[combo_value])
        except KeyError:
            return None  # Si no se encuentra la clave, no se carga ninguna imagen

    # Cargar la imagen inicial
    image = cargar_imagen(combo_value)

    # Función para guardar la captura de pantalla en el escritorio
    def guardar_imagen_en_escritorio():
        # Obtener la ruta de la carpeta de videos
        videos_path = os.path.join(os.path.expanduser("~"), "Videos", "HappyNewYear.png")
    
        # Guardar la imagen
        pygame.image.save(screen, videos_path)
        print(f"Imagen guardada en: {videos_path}")
    
        return videos_path  # Devuelve la ruta de la imagen guardada para mostrarla

    # Bucle principal
    state = "fixed_name"  # Estado inicial
    image_shown = False  # Bandera para saber si mostrar la imagen
    button_shown = False  # Bandera para saber si mostrar el botón
    button_rect = pygame.Rect(50, 750, 200, 40)  # Botón en la parte inferior izquierda
    ruta_texto = ""
    image_path = None
    ruta_mostrada_time = None  # Variable para controlar el tiempo que se muestra la ruta
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Detectar clic en el botón
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    image_path = guardar_imagen_en_escritorio()  # Guardar la imagen cuando se hace clic en el botón
                    ruta_texto = f"Imagen guardada en: {image_path}"
                    ruta_mostrada_time = pygame.time.get_ticks()  # Establecer el tiempo de cuando se mostró la ruta

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
                button_shown = True  # Muestra el botón después de la animación

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

        # Mostrar el botón solo después de la animación
        if button_shown:
            # Dibujar solo el texto del botón, sin fondo
            button_text = pygame.font.Font(font_path, 36).render("Descargar imagen", True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, button_text_rect)
            
        # Mostrar la ruta donde se guardó la imagen (y desaparecerla después de 3 segundos)
        if image_path and ruta_mostrada_time:
            # Mostrar la ruta
            ruta_surface = font1.render(ruta_texto, True, WHITE)
            ruta_rect = ruta_surface.get_rect(center=(800 // 2, 750))  # Ajuste de la posición de la ruta
            screen.blit(ruta_surface, ruta_rect)

            # Eliminar mensaje después de 3 segundos
            if current_time - ruta_mostrada_time >= 3000:  # 3000 milisegundos = 3 segundos
                ruta_texto = ""
                ruta_mostrada_time = None

        pygame.display.flip()
        clock.tick(60)

# Ejecuta la animación
# animate_name("Oscar", "Best Wishes")
