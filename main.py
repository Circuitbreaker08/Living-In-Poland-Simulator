import pygame

import assets

pygame.init()
screen = pygame.dislay.setmode((1920, 1080))
pygame.display.setcaption("Living In Poland Simulator")

running = True
while running:
    for event in pygame.events.get():
        if event == pygame.QUIT:
            running = False