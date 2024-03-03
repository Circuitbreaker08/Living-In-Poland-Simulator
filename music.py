from pygame.mixer import music as player
import threading
import random
import sys
import os

if getattr(sys.modules["__main__"], 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

root = os.getcwd()
os.chdir(os.path.join(root, "assets/music"))
songs = os.listdir()

def play():
    try:
        while True:
            if not player.get_busy():
                file = os.path.join(root, "assets/music", songs[random.randint(0, len(songs) - 1)])
                player.load(file)
                player.play()
    except:
        pass

threading.Thread(target = play).start()