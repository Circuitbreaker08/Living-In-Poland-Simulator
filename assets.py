"""
Loads everything into memory at the start of runtime
"""

import pygame
import json
import os
import sys

if getattr(sys.modules["__main__"], 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

sprites = {}
maps = {}

root = os.getcwd()
os.chdir("assets/sprites")

for directory in os.listdir():
    sprites.update({directory: {}})
    os.chdir(os.path.join(root, "assets/sprites", directory))
    if directory == "portraits":
        size = (256, 256)
    else:
        size = (64, 64)
    for file in os.listdir():
        sprites[directory].update({file: pygame.transform.scale(pygame.image.load(file).convert_alpha(), size)})

os.chdir(os.path.join(root, "assets/maps"))

for file in os.listdir():
    with open(file) as f:
        maps.update({file: json.loads(f.read())})

print(root)
os.chdir(root)