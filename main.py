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
import hacking

is_chatting = False
is_coding = False
is_hacking = False
chat_cooldown = 0
loaded_map = "test_room_1.json"
position = [2 * 64, 2 * 64]

def move(x, y):
    global position
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

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))

    for zone in maps[loaded_map]["triggers"]:
        if position[0] + 64 > zone["x"] * 64 and position[0] < zone["x"] * 64 + 64 and position[1] + 64 > zone["y"] * 64 and position[1] < zone["y"] * 64 + 64:
            exec(zone["code"])
            break
                 
    if not (is_chatting or is_coding or is_hacking):
        move(
            3 * (pygame.key.get_pressed()[pygame.K_d] - pygame.key.get_pressed()[pygame.K_a]),
            3 * (pygame.key.get_pressed()[pygame.K_s] - pygame.key.get_pressed()[pygame.K_w])
        )

    for tile in maps[loaded_map]["floors"] + maps[loaded_map]["walls"]:
        screen.blit(sprites["mapping"][tile["sprite"]], (tile["x"] * 64 + 960 - position[0], tile["y"] * 64 + 540 - position[1]))

    screen.blit(sprites["characters"]["debug.png"], (960, 540))

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

    pygame.display.flip()
    clock.tick(60)