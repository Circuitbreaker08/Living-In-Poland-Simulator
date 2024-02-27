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

    screen.blit(pygame.font.Font(None, 24).render("Target Agression", False, (25, 25, 170)), (310, 445))
    screen.blit(pygame.font.Font(None, 24).render("Actual Agression", False, (230, 0, 0)), (310, 465))

    img = pygame.font.Font(None, 48).render("Hack Agression", False, (255, 255, 255))
    screen.blit(img, (960 - img.get_width()/2, 400))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((500, 450), (970, 30)), width=1)

    img = pygame.font.Font(None, 48).render(f"{int(progress/goal)}%", False, (255, 255, 255))
    screen.blit(img, (960 - img.get_width()/2, 600))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((500, 650), (970, 30)), width=1)
    pygame.draw.rect(screen, (0, 255, 0), pygame.rect.Rect((500, 650), ((progress/goal) * 970, 30)))