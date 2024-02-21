import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Living In Poland Simulator")

from assets import sprites, maps

chatting = False
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

    screen.fill((0, 0, 0))

    for zone in maps[loaded_map]["loading_zones"]:
        if position[0] + 64 > zone["x"] * 64 and position[0] < zone["x"] * 64 + 64 and position[1] + 64 > zone["y"] * 64 and position[1] < zone["y"] * 64 + 64:
            loaded_map = zone["target_map"]
            position = [zone["target_x"] * 64, zone["target_y"] * 64]
            break

    if not chatting:
        move(
            3 * (pygame.key.get_pressed()[pygame.K_d] - pygame.key.get_pressed()[pygame.K_a]),
            3 * (pygame.key.get_pressed()[pygame.K_s] - pygame.key.get_pressed()[pygame.K_w])
        )

    for tile in maps[loaded_map]["floors"] + maps[loaded_map]["walls"]:
        screen.blit(sprites["mapping"][tile["sprite"]], (tile["x"] * 64 + 960 - position[0], tile["y"] * 64 + 540 - position[1]))

    screen.blit(sprites["characters"]["debug.png"], (960, 540))

    for npc in maps[loaded_map]["npcs"]:
        screen.blit(sprites["characters"][npc["sprite"]], (npc["x"] * 64 + 960 - position[0], npc["y"] * 64 + 540 - position[1]))
        if not chatting and pygame.key.get_pressed()[pygame.K_SPACE] and 128 >= math.dist(position, (npc["x"] * 64, npc["y"] * 64)) and chat_cooldown < time.time():
            chatting = True
            portrait = sprites["portraits"][npc["portrait"]]
            messages = npc["dialogue"]
            num_messages = 0
            chat_cooldown = time.time() + 0.1
            break

    if chatting:
        pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect((190, 690), (1540, 276)))
        pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect((190, 690), (1540, 276)), width=5)
        screen.blit(portrait, (200, 700))
        screen.blit(pygame.font.Font(None, 48).render(messages[num_messages], False, (255, 255, 255)), (500, 800))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and chat_cooldown < time.time():
                    num_messages += 1
                    print(num_messages)
                    if num_messages >= len(messages):
                        chat_cooldown = time.time() + 1
                        chatting = False

    pygame.display.flip()
    clock.tick(60)