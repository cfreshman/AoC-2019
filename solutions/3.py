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
# simple solution: traverse along each wire tile by tile
DIRS = {'R': [1, 0], 'U': [0, 1], 'L': [-1, 0], 'D': [0, -1]}

# store first wire positions in set
pos = (0, 0)
wires = set()
for wire in lines[0].split(','):
    d, n = DIRS[wire[0]], int(wire[1:])
    for i in range(n):
        pos = (pos[0] + d[0], pos[1] + d[1])
        wires.add(pos)

# check second wire positions against set
pos = (0, 0)
min_dist = math.inf
for wire in lines[1].split(','):
    d, n = DIRS[wire[0]], int(wire[1:])
    for i in range(n):
        pos = (pos[0] + d[0], pos[1] + d[1])
        if pos in wires:
            min_dist = min(min_dist, abs(pos[0]) + abs(pos[1]))

print(min_dist)

# --- Part Two ---
# same as part 1 except use dict with # steps taken
pos = (0, 0)
step = 0
steps = {}
for wire in lines[0].split(','):
    d, n = DIRS[wire[0]], int(wire[1:])
    for i in range(n):
        pos = (pos[0] + d[0], pos[1] + d[1])
        step += 1
        steps[pos] = step

pos = (0, 0)
step = 0
min_steps = math.inf
for wire in lines[1].split(','):
    d, n = DIRS[wire[0]], int(wire[1:])
    for i in range(n):
        pos = (pos[0] + d[0], pos[1] + d[1])
        step += 1
        if pos in steps:
            min_steps = min(min_steps, steps[pos] + step)

print(min_steps)