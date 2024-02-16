import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Living In Poland Simulator")

from assets import sprites, maps

loaded_map = "test_room_1.json"
position = [128, 128]

def move(x, y):
    global position
    """
    for wall in maps[loaded_map]["walls"]:
        if pygame.Rect((position[0], position[1]), (position[0] + 64, position[1] + 64)).colliderect(pygame.Rect()):
            break
    else:
        position[0] += x

    for wall in maps[loaded_map]["walls"]:
        if False:
            break
    else:
        position[1] += y
    """
        
def chat(message, portrait):
    portrait = sprites["portraits"][portrait]
    screen.blit(portrait, (200, 700))
    screen.blit(pygame.font.Font(None, 48).render(message, False, (255, 255, 255)), (500, 800))

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    move(
        3 * (pygame.key.get_pressed()[pygame.K_d] - pygame.key.get_pressed()[pygame.K_a]),
        3 * (pygame.key.get_pressed()[pygame.K_s] - pygame.key.get_pressed()[pygame.K_w])
    )

    for tile in maps[loaded_map]["floors"] + maps[loaded_map]["walls"]:
        screen.blit(sprites["mapping"][tile["sprite"]], (tile["x"] * 64 + 960 - position[0], tile["y"] * 64 + 540 - position[1]))

    screen.blit(sprites["characters"]["debug.png"], (960, 540))

    chat("Hi, Polski-san!", "bocchi_1000_yard_stare.png")

    pygame.display.flip()
    clock.tick(60)