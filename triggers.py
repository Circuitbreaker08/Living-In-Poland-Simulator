import sys

def move(position, map):
    setattr(sys.modules["__main__"], "position", [position[0] * 64, position[1] * 64])
    setattr(sys.modules["__main__"], "loaded_map", map)