import pygame
import math
import json
import sys
import os

boolean_color = {False: (255, 0, 0), True: (0, 255, 0)}

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

floor_visible = True
wall_visible = True
trigger_visible = True

from assets import sprites

os.chdir(os.path.join(root, "assets/maps"))
with open(file) as f:
    data = json.loads(f.read())

running = True
while running:
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    mouse_down = False
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True

    screen.fill((0, 0, 0))

    position[0] += (pygame.key.get_pressed()[pygame.K_LSHIFT] * 10 + 3) * (pygame.key.get_pressed()[pygame.K_d] - pygame.key.get_pressed()[pygame.K_a])
    position[1] += (pygame.key.get_pressed()[pygame.K_LSHIFT] * 10 + 3) * (pygame.key.get_pressed()[pygame.K_s] - pygame.key.get_pressed()[pygame.K_w])

    if floor_visible:
        for tile in data["floors"]:
            screen.blit(sprites["mapping"][tile["sprite"]], (tile["x"] * 64 + 960 - position[0], tile["y"] * 64 + 540 - position[1]))

    if wall_visible:
        for tile in data["walls"]:
            screen.blit(sprites["mapping"][tile["sprite"]], (tile["x"] * 64 + 960 - position[0], tile["y"] * 64 + 540 - position[1]))

    if trigger_visible:
        for trigger in data["triggers"]:
            pygame.draw.rect(screen, (0, 0, 200, 50), pygame.rect.Rect((trigger["x"] * 64 + 960 - position[0], trigger["y"] * 64 + 540 - position[1]), (64, 64)))    

    mouse_world = [mouse[0] - 960 + position[0], mouse[1] - 540 + position[1]]
    tile = [math.floor(mouse_world[0] / 64), math.floor(mouse_world[1] / 64)]
    pygame.draw.rect(screen, (0, 200, 0, 50), pygame.rect.Rect((tile[0] * 64 + 960 - position[0], tile[1] * 64 + 540 - position[1]), (64, 64)))
    screen.blit(pygame.font.Font(None, 48).render(str(tuple(tile)), False, (255, 255, 255)), (0, 70))

    screen.blit(pygame.font.Font(None, 48).render("Quit", False, (255, 255, 255)), (0, 0))
    if mouse_down and mouse[0] > 0 and mouse[0] < 70 and mouse[1] > 0 and mouse[1] < 33:
        running = False
    screen.blit(pygame.font.Font(None, 48).render("Save", False, (255, 255, 255)), (0, 33))
    if mouse_down and mouse[0] > 0 and mouse[0] < 70 and mouse[1] > 33 and mouse[1] < 66:
        running = False

    screen.blit(pygame.font.Font(None, 48).render("Toggle Trigger View", False, boolean_color[trigger_visible]), (0, 99))
    if mouse_down and mouse[0] > 0 and mouse[0] < 500 and mouse[1] > 99 and mouse[1] < 132:
        trigger_visible = not trigger_visible
    screen.blit(pygame.font.Font(None, 48).render("Toggle Floor View", False, boolean_color[floor_visible]), (0, 132))
    if mouse_down and mouse[0] > 0 and mouse[0] < 500 and mouse[1] > 132 and mouse[1] < 165:
        floor_visible = not floor_visible   
    screen.blit(pygame.font.Font(None, 48).render("Toggle Wall View", False, boolean_color[wall_visible]), (0, 165))
    if mouse_down and mouse[0] > 0 and mouse[0] < 500 and mouse[1] > 165 and mouse[1] < 198:
        wall_visible = not wall_visible

    pygame.display.flip()
    clock.tick(60)