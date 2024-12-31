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

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

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
