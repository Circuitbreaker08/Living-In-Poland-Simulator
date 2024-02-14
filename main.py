import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Living In Poland Simulator")

import assets

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    clock.tick(60)