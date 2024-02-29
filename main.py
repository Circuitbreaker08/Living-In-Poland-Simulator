import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Living In Poland Simulator")

from assets import sprites, maps
import triggers
import coding
import inventory
import hacking
import music

music.start()

satiation = 0
money = 100

is_chatting = False
is_coding = False
is_hacking = False
is_shopping = False
inventory_open = False

chat_cooldown = 0
loaded_map = "test_room_1.json"
position = [2 * 64, 2 * 64]
rotation = 0

def move(x, y):
    global position, rotation
    position[0] += x
    for wall in maps[loaded_map]["walls"] + maps[loaded_map]["npcs"]:
        if position[0] + 64 > wall["x"] * 64 and position[0] < wall["x"] * 64 + 64 and position[1] + 64 > wall["y"] * 64 and position[1] < wall["y"] * 64 + 64:
            position[0] -= x
            break

    position[1] += y
    for wall in maps[loaded_map]["walls"] + maps[loaded_map]["npcs"]:
        if position[0] + 64 > wall["x"] * 64 and position[0] < wall["x"] * 64 + 64 and position[1] + 64 > wall["y"] * 64 and position[1] < wall["y"] * 64 + 64:
            position[1] -= y
            break

    if abs(x) > abs(y) and x > 0:
        rotation = 270
    elif abs(x) > abs(y) and x < 0:
        rotation = 90
    elif abs(y) > abs(x) and y > 0:
        rotation = 180
    elif abs(y) > abs(x) and y < 0:
        rotation = 0

running = True
while running:
    mouse_down = False
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                inventory_open = not inventory_open

    mouse = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))

    for zone in maps[loaded_map]["triggers"]:
        if position[0] + 64 > zone["x"] * 64 and position[0] < zone["x"] * 64 + 64 and position[1] + 64 > zone["y"] * 64 and position[1] < zone["y"] * 64 + 64:
            exec(zone["code"])
            break
                 
    if not (is_chatting or is_coding or is_hacking or is_shopping) or inventory_open:
        move(
            3 * (pygame.key.get_pressed()[pygame.K_d] - pygame.key.get_pressed()[pygame.K_a]),
            3 * (pygame.key.get_pressed()[pygame.K_s] - pygame.key.get_pressed()[pygame.K_w])
        )

    for tile in maps[loaded_map]["floors"] + maps[loaded_map]["walls"]:
        screen.blit(sprites["mapping"][tile["sprite"]], (tile["x"] * 64 + 960 - position[0], tile["y"] * 64 + 540 - position[1]))

    screen.blit(pygame.transform.rotate(sprites["characters"]["mc.png"], rotation), (960, 540))

    for npc in maps[loaded_map]["npcs"]:
        screen.blit(sprites["characters"][npc["sprite"]], (npc["x"] * 64 + 960 - position[0], npc["y"] * 64 + 540 - position[1]))
        if not (is_chatting or is_coding or is_hacking) and pygame.key.get_pressed()[pygame.K_SPACE] and 100 >= math.dist(position, (npc["x"] * 64, npc["y"] * 64)) and chat_cooldown < time.time():
            is_chatting = True
            messages = npc["lines"]
            num_messages = 0
            chat_cooldown = time.time() + 0.1
            break

    if is_chatting:
        pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect((190, 690), (1540, 276)))
        pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((190, 690), (1540, 276)), width=5)
        screen.blit(sprites["portraits"][messages[num_messages]["image"]], (200, 700))
        screen.blit(pygame.font.Font(None, 48).render(messages[num_messages]["text"], False, (255, 255, 255)), (500, 800))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and chat_cooldown < time.time():
                    try:
                        exec(messages[num_messages]["code"])
                    except:
                        pass
                    num_messages += 1
                    if num_messages >= len(messages):
                        chat_cooldown = time.time() + 1
                        is_chatting = False

    if is_coding:
        coding.code()

    if is_hacking:
        hacking.hack()

    if inventory_open:
        inventory.inventory()

    if is_shopping:
        inventory.shop()

    screen.blit(pygame.font.Font(None, 48).render(f"Satiation: {int(satiation)}", False, (255, 255, 255)), (10, 10))
    screen.blit(pygame.font.Font(None, 48).render(f"{money}zł", False, (255, 255, 255)), (10, 50))

    satiation -= 0.001

    pygame.display.flip()
    clock.tick(60)