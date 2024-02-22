import pygame
import math
import json
import sys
import os

try:
    file = sys.argv[1]
except:
    file = input("Map Filename")
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Polegrid")
root = os.getcwd()
position = [0, 0]

from assets import sprites

os.chdir(os.path.join(root, "assets/maps"))
with open(file) as f:
    data = json.loads(f.read())

running = True
while running:
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    for event in events:
        if event == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    screen.blit(pygame.font.Font(None, 48).render("Quit", False, (255, 255, 255)), (0, 0))
    if pygame.mouse.get_pressed()[0] and mouse[0] > 0 and mouse[0] < 70 and mouse[1] > 0 and mouse[1] < 33:
        running = False
    screen.blit(pygame.font.Font(None, 48).render("Save", False, (255, 255, 255)), (0, 33))
    if pygame.mouse.get_pressed()[0] and mouse[0] > 0 and mouse[0] < 70 and mouse[1] > 33 and mouse[1] < 66:
        running = False

    position[0] += 3 * (pygame.key.get_pressed()[pygame.K_d] - pygame.key.get_pressed()[pygame.K_a])
    position[1] += 3 * (pygame.key.get_pressed()[pygame.K_s] - pygame.key.get_pressed()[pygame.K_w])

    for tile in data["floors"] + data["walls"]:
        screen.blit(sprites["mapping"][tile["sprite"]], (tile["x"] * 64 + 960 - position[0], tile["y"] * 64 + 540 - position[1]))

    mouse_world = [mouse[0] - 960 + position[0], mouse[1] - 540 + position[1]]
    tile = [math.floor(mouse_world[0] / 64), math.floor(mouse_world[1] / 64)]
    pygame.draw.rect(screen, (0, 200, 0, 50), pygame.rect.Rect((tile[0] * 64 + 960 - position[0], tile[1] * 64 + 540 - position[1]), (64, 64)))
    screen.blit(pygame.font.Font(None, 48).render(str(tuple(tile)), False, (255, 255, 255)), (0, 70))

    pygame.display.flip()
    clock.tick(60)