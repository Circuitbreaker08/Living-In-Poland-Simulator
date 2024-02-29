import pygame
import sys

from assets import sprites

screen: pygame.Surface = getattr(sys.modules["__main__"], "screen")

items = {
    "ciastka_miodowe": 0,
    "kielbasa": 0,
    "pierogie": 0,
    "tartar": 0
}

def shop():
    money = getattr(sys.modules["__main__"], "money")

    mouse = pygame.mouse.get_pos()
    mouse_down = getattr(sys.modules["__main__"], "mouse_down")

    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect((250, 250), (1420, 580)))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((250, 250), (1420, 580)), width=5)

    screen.blit(pygame.font.Font(None, 48).render("10zł", False, (255, 255, 255)), (300, 300))
    screen.blit(sprites["items"]["ciastka_miodowe.png"], (400, 300))
    if mouse[0] > 300 and mouse[0] < 464 and mouse[1] > 300 and mouse[1] < 364 and mouse_down and money - 10 >= 0:
        setattr(sys.modules["__main__"], "money", money - 10)
        items["ciastka_miodowe"] += 1

    screen.blit(pygame.font.Font(None, 48).render("20zł", False, (255, 255, 255)), (300, 400))
    screen.blit(sprites["items"]["kielbasa.png"], (400, 400))
    if mouse[0] > 300 and mouse[0] < 464 and mouse[1] > 400 and mouse[1] < 464 and mouse_down and money - 20 >= 0:
        setattr(sys.modules["__main__"], "money", money - 20)
        items["kielbasa"] += 1

    screen.blit(pygame.font.Font(None, 48).render("5zł", False, (255, 255, 255)), (500, 300))
    screen.blit(sprites["items"]["pierogie.png"], (600, 300))
    if mouse[0] > 500 and mouse[0] < 664 and mouse[1] > 300 and mouse[1] < 364 and mouse_down and money - 5 >= 0:
        setattr(sys.modules["__main__"], "money", money - 5)
        items["pierogie"] += 1

    screen.blit(pygame.font.Font(None, 48).render("30zł", False, (255, 255, 255)), (500, 400))
    screen.blit(sprites["items"]["tartar.png"], (600, 400))
    if mouse[0] > 500 and mouse[0] < 664 and mouse[1] > 400 and mouse[1] < 464 and mouse_down and money - 30 >= 0:
        setattr(sys.modules["__main__"], "money", money - 30)
        items["tartar"] += 1

    screen.blit(pygame.font.Font(None, 48).render("Close", False, (255, 255, 255)), (1550, 790))
    if mouse[0] > 1550 and mouse[0] < 1670 and mouse[1] > 250 and mouse[1] < 830 and mouse_down:
        setattr(sys.modules["__main__"], "is_shopping", False)

def inventory():
    satiation = getattr(sys.modules["__main__"], "satiation")

    mouse = pygame.mouse.get_pos()
    mouse_down = getattr(sys.modules["__main__"], "mouse_down")

    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect((250, 250), (1420, 580)))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((250, 250), (1420, 580)), width=5)

    screen.blit(pygame.font.Font(None, 48).render(f"x {items['ciastka_miodowe']}", False, (255, 255, 255)), (300, 300))
    screen.blit(sprites["items"]["ciastka_miodowe.png"], (400, 300))
    if mouse[0] > 300 and mouse[0] < 464 and mouse[1] > 300 and mouse[1] < 364 and mouse_down and items["ciastka_miodowe"] > 0:
        setattr(sys.modules["__main__"], "satiation", min(satiation + 10, 100))
        items["ciastka_miodowe"] -= 1

    screen.blit(pygame.font.Font(None, 48).render(f"x {items['kielbasa']}", False, (255, 255, 255)), (300, 400))
    screen.blit(sprites["items"]["kielbasa.png"], (400, 400))
    if mouse[0] > 300 and mouse[0] < 464 and mouse[1] > 400 and mouse[1] < 464 and mouse_down and items["kielbasa"] > 0:
        setattr(sys.modules["__main__"], "satiation", min(satiation + 20, 100))
        items["kielbasa"] -= 1

    screen.blit(pygame.font.Font(None, 48).render(f"x {items['pierogie']}", False, (255, 255, 255)), (500, 300))
    screen.blit(sprites["items"]["pierogie.png"], (600, 300))
    if mouse[0] > 500 and mouse[0] < 664 and mouse[1] > 300 and mouse[1] < 364 and mouse_down and items["pierogie"] > 0:
        setattr(sys.modules["__main__"], "satiation", min(satiation + 5, 100))
        items["pierogie"] -= 1

    screen.blit(pygame.font.Font(None, 48).render(f"x {items['tartar']}", False, (255, 255, 255)), (500, 400))
    screen.blit(sprites["items"]["tartar.png"], (600, 400))
    if mouse[0] > 500 and mouse[0] < 664 and mouse[1] > 400 and mouse[1] < 464 and mouse_down and items["tartar"] > 0:
        setattr(sys.modules["__main__"], "satiation", min(satiation + 30), 100)
        items["tartar"] -= 1