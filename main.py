import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Living In Poland Simulator")

from assets import sprites, maps

chatting = False
loaded_map = "test_room_1.json"
position = [128, 128]

def move(x, y):
    global position
    position[0] += x
    for wall in maps[loaded_map]["walls"]:
        if position[0] + 64 > wall["x"] * 64 and position[0] < wall["x"] * 64 + 64 and position[1] + 64 > wall["y"] * 64 and position[1] < wall["y"] * 64 + 64:
            position[0] -= x
            break

    position[1] += y
    for wall in maps[loaded_map]["walls"]:
        if position[0] + 64 > wall["x"] * 64 and position[0] < wall["x"] * 64 + 64 and position[1] + 64 > wall["y"] * 64 and position[1] < wall["y"] * 64 + 64:
            position[1] -= y
            break
        
def chat(message, portrait):
    global chatting
    chatting = True
    portrait = sprites["portraits"][portrait]
    screen.blit(portrait, (200, 700))
    screen.blit(pygame.font.Font(None, 48).render(message, False, (255, 255, 255)), (500, 800))

running = True
while running:
    for event in pygame.event.get():
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

    if False:
        chat("Hi, Polski-san!", "bocchi_1000_yard_stare.png")

    pygame.display.flip()
    clock.tick(60)