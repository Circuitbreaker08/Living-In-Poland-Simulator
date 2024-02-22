"""
Loads everything into memory at the start of runtime
"""

import pygame
import json
import os

sprites = {}
maps = {}

os.chdir(os.path.join(os.path.split(__file__)[0], "assets/sprites"))
root = os.getcwd()

for directory in os.listdir():
    sprites.update({directory: {}})
    os.chdir(os.path.join(root, directory))
    if directory == "portraits":
        size = (256, 256)
    else:
        size = (64, 64)
    for file in os.listdir():
        sprites[directory].update({file: pygame.transform.scale(pygame.image.load(file).convert_alpha(), size)})

os.chdir(os.path.join(os.path.split(__file__)[0], "assets/maps"))
root = os.getcwd()

for file in os.listdir():
    with open(file) as f:
        maps.update({file: json.loads(f.read())})

