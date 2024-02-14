import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Living In Poland Simulator")

from assets import sprites, maps

loaded_map = "test_room_1.json"

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    for tile in maps[loaded_map]["floors"] + maps[loaded_map]["walls"]:
        screen.blit(sprites["mapping"][tile["sprite"]], (tile["x"] * 32 + 960, tile["y"] * 32 + 540))

    screen.blit(sprites["characters"]["debug.png"], (960, 540))

    pygame.display.flip()
    clock.tick(60)