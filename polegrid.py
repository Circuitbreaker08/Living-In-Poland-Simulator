import pygame
import json
import sys
import os

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Polegrid")
root = os.getcwd()
file = sys.argv[1]
position = [0, 0]

from assets import sprites

os.chdir(os.path.join(root, "assets/maps"))
with open(file) as f:
    data = json.loads(f.read())

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    position[0] += 3 * (pygame.key.get_pressed()[pygame.K_d] - pygame.key.get_pressed()[pygame.K_a])
    position[1] += 3 * (pygame.key.get_pressed()[pygame.K_s] - pygame.key.get_pressed()[pygame.K_w])

    for tile in data["floors"] + data["walls"]:
        screen.blit(sprites["mapping"][tile["sprite"]], (tile["x"] * 64 + 960 - position[0], tile["y"] * 64 + 540 - position[1]))

    pygame.display.flip()
    clock.tick(60)