import pygame
import random
import sys

from assets import sprites

screen: pygame.Surface = getattr(sys.modules["__main__"], "screen")

def init():
    global initialized, goal, progress
    initialized = True
    goal = 10
    progress = -1
    shuffle()

def shuffle():
    global file, progress
    file = (random.randint(314, 1606), random.randint(314, 516))
    progress += 1
    if progress == goal:
        finish()

def finish():
    setattr(sys.modules["__main__"], "is_coding", False)

def code():
    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect((250, 250), (1420, 580)))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((250, 250), (1420, 580)), width=5)

    img = pygame.font.Font(None, 48).render(f"Lines: {progress}/{goal}", False, (255, 255, 255))
    screen.blit(img, (960 - img.get_width()/2, 300))

    screen.blit(sprites["coding"]["file.png"], file)

    mouse = getattr(sys.modules["__main__"], "mouse")
    if mouse[0] > file[0] and mouse[0] < file[0] + 64 and mouse[1] > file[1] and mouse[1] < file[1] + 64 and pygame.mouse.get_pressed()[0]:
        shuffle()

init()