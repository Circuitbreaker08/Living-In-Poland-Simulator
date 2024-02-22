import sys

def move(position, map):
    #_position = getattr(sys.modules["__main__"], "position")
    #_loaded_map = getattr(sys.modules["__main__"], "loaded_map")
    setattr(sys.modules["__main__"], "position", [position[0] * 64, position[1] * 64])
    setattr(sys.modules["__main__"], "loaded_map", map)