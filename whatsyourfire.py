import math
import random
import pygame
import sys

# Inicialización
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
particles = [(random.gauss(0, .5), random.uniform(0, 6.28318)) for _ in range(2500)]
colors = [[255, 0, 255], [7, 185, 252], [0, 171, 56], [154, 240, 0], [255, 230, 50], [255, 130, 42], [255, 0, 0]]
font = pygame.font.SysFont(None, 36)

# Botón "Salir"
button_rect = pygame.Rect(650, 730, 120, 40)

# Funciones
def dibujar_boton():
    pygame.draw.rect(screen, (200, 0, 0), button_rect)
    text_surface = font.render("Salir", True, (255, 255, 255))
    screen.blit(text_surface, (button_rect.x + 25, button_rect.y + 5))

def secuencia_explosiones():
    coordx = 100
    color = 0
    while True:  # Bucle principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Explosión aleatoria
        coordy = random.randint(100, 700)
        radio = random.randint(100, 250)
        explotar(coordx, coordy, radio, colors[color])
        color = (color + 1) % len(colors)
        coordx += 120
        if coordx > 700:
            coordx = 100

def explotar(posx, posy, radio, color):
    print(f"Explosión en X={posx}, Y={posy}, Radio={radio}")
    for i in range(radio):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.fill((0, 0, 0))
        dibujar_boton()  # Dibuja el botón "Salir"
        for speed, angle in particles:
            distance = i * speed
            x = posx + distance * math.cos(angle)
            y = posy + distance * math.sin(angle)
            if 0 <= x < 800 and 0 <= y < 800:  # Verifica límites
                screen.set_at((int(x), int(y)), color)
        pygame.display.flip()
        clock.tick(60)  # Control de FPS

# Ejecución principal
secuencia_explosiones()
pygame.quit()
