"""
Loads everything into memory at the start of runtime
"""

import os

sprites = {}
root = os.getcwd()

os.cwd(os.path.join(root, "assets/sprites"))
for dir in os.listdir():
    pass