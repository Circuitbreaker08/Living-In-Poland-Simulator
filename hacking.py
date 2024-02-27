import pygame
import sys

screen: pygame.Surface = getattr(sys.modules["__main__"], "screen")

def init():
    global progress, goal
    progress = 0
    goal = 100

def finish():
    setattr(sys.modules["__main__"], "is_hacking", False)

def hack():
    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect((250, 250), (1420, 580)))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((250, 250), (1420, 580)), width=5)

    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((500, 450), (970, 30)), width=1)

    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((500, 650), (970, 30)), width=1)
    pygame.draw.rect(screen, (0, 255, 0), pygame.rect.Rect((500, (progress/goal) * 650), (970, 30)))