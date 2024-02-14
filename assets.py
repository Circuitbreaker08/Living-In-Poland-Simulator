"""
Loads everything into memory at the start of runtime
"""

import os
import pygame

pygame.display.init()
os.chdir(os.path.join(os.path.split(__file__)[0], "assets/sprites"))
root = os.getcwd()
print(root)
sprites = {}

for directory in os.listdir():
    sprites.update({directory: {}})
    os.chdir(os.path.join(root, directory))
    for file in os.listdir():
        sprites[directory].update({file: pygame.image.load(file).convert_alpha()})