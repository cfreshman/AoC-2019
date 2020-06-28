import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

import math
import re
import itertools
import datetime
import heapq
from collections import namedtuple

# --- Part One ---
width = 25
height = 6
image = lines[0]

layer_size = width * height
layers = [image[i:i+layer_size] for i in range(0, len(image), layer_size)]

# layer with min zeros
layer_z = min(layers, key=lambda l: len([x for x in l if x == '0']))
print(len([x for x in layer_z if x == '1']) * len([x for x in layer_z if x == '2']))

# --- Part Two ---
final = list(layers[0])
for i in range(layer_size):
    for j in range(len(layers)):
        if layers[j][i] != '2':
            final[i] = {'0': '█', '1': ' '}[layers[j][i]]
            break

final = [final[i:i+width] for i in range(0, len(final), width)]
[print(''.join(row)) for row in final]