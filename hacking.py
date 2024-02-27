import pygame
import random
import sys

screen: pygame.Surface = getattr(sys.modules["__main__"], "screen")

def init():
    global target, target_range, actual, progress, goal
    target = 45
    target_range = 50
    actual = 50
    progress = 20
    goal = 100

def victory():
    finish()

def defeat():
    finish()

def finish():
    setattr(sys.modules["__main__"], "is_hacking", False)

def hack():
    global actual, progress
    if pygame.mouse.get_pressed()[0]:
        actual = min(actual + 3, 959)
    else:
        actual = max(actual - 3, 1)

    if actual > target and actual < target + target_range:
        progress += 1.5
    else:
        progress -= 0.5

    if progress >= 100:
        victory()
    elif progress <= 0:
        defeat()

    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect((250, 250), (1420, 580)))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((250, 250), (1420, 580)), width=5)

    screen.blit(pygame.font.Font(None, 24).render("Target Agression", False, (25, 25, 170)), (310, 445))
    screen.blit(pygame.font.Font(None, 24).render("Actual Agression", False, (230, 0, 0)), (310, 465))

    img = pygame.font.Font(None, 48).render("Hack Agression", False, (255, 255, 255))
    screen.blit(img, (960 - img.get_width()/2, 400))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((500, 450), (970, 30)), width=1)

    pygame.draw.rect(screen, (25, 25, 170), pygame.rect.Rect((500 + target, 451), (target_range, 28)))
    pygame.draw.rect(screen, (230, 0, 0), pygame.rect.Rect((500 + actual, 451), (10, 28)))

    img = pygame.font.Font(None, 48).render(f"{int(progress/goal * 100)}%", False, (255, 255, 255))
    screen.blit(img, (960 - img.get_width()/2, 600))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((500, 650), (970, 30)), width=1)
    pygame.draw.rect(screen, (0, 255, 0), pygame.rect.Rect((500, 650), ((progress/goal) * 970, 30)))