import sys

import coding
import hacking
import inventory

def move(position, map):
    setattr(sys.modules["__main__"], "position", [position[0] * 64, position[1] * 64])
    setattr(sys.modules["__main__"], "loaded_map", map)

def init_coding():
    setattr(sys.modules["__main__"], "is_coding", True)
    coding.init()

def init_hacking():
    setattr(sys.modules["__main__"], "is_hacking", True)
    hacking.init()

def init_shopping():
    setattr(sys.modules["__main__"], "is_shopping", True)
    inventory.init_shopping()