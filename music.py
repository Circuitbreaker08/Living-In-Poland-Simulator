import pygame.mixer.music as player
import threading
import random
import sys
import os

if getattr(sys.modules["__main__"], 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

root = os.getcwd()
os.chdir("assets/music")
songs = os.listdir()

def play():
    while True:
        if not player.get_busy():
            player.play(os.path.join(root, songs[random.randint(len(songs))]))

threading.Thread(target = play).start()