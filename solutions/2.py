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
ints = [int(x) for x in lines[0].split(',')]
ints[1] = 12
ints[2] = 2

index = 0
while ints[index] != 99:
    opcode, i_arg1, i_arg2, i_out = ints[index:index+4]
    arg1, arg2 = ints[i_arg1], ints[i_arg2]
    ints[i_out] = (arg1 + arg2) if opcode == 1 else (arg1 * arg2)
    index += 4
print(ints)

# --- Part Two ---
target = 19690720
for noun in range(100):
    for verb in range(100):
        ints = [int(x) for x in lines[0].split(',')]
        ints[1] = noun
        ints[2] = verb

        index = 0
        while ints[index] != 99:
            opcode, i_arg1, i_arg2, i_out = ints[index:index+4]
            arg1, arg2 = ints[i_arg1], ints[i_arg2]
            ints[i_out] = (arg1 + arg2) if opcode == 1 else (arg1 * arg2)
            index += 4

        if ints[0] == target:
            print(100*noun + verb)
            exit(0)