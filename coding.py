import pygame
import sys

screen = getattr(sys.modules["__main__"], "screen")

def init():
    goal = 40
    progress = 0

def code():
    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect((250, 250), (1420, 580)))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((250, 250), (1420, 580)), width=5)

    img = pygame.font.Font(None, 48).render("Lines", False, (255, 255, 255))
    screen.blit(img, (960 - img.get_width()/2, 300))