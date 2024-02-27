import pygame
import sys

from assets import sprites

screen: pygame.Surface = getattr(sys.modules["__main__"], "screen")

def init():
    global progress, goal
    progress = 0
    goal = 0

def shuffle():
    pass


def finish():
    setattr(sys.modules["__main__"], "is_hacking", False)

def hack():
    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect((250, 250), (1420, 580)))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((250, 250), (1420, 580)), width=5)

    img = pygame.font.Font(None, 48).render(f"Lines: {progress}/{goal}", False, (255, 255, 255))
    screen.blit(img, (960 - img.get_width()/2, 300))