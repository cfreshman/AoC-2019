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
inputs = [1]
outputs = []

index = 0
while ints[index] != 99:
    opcode = ints[index]
    modes = [int(s) for s in ('000' + str(opcode))[-3::-1]]
    opcode = int(str(opcode)[-1])
    if opcode == 1 or opcode == 2:
        i_arg1, i_arg2, i_out = ints[index+1:index+4]
        arg1 = ints[i_arg1] if modes[0] == 0 else i_arg1
        arg2 = ints[i_arg2] if modes[1] == 0 else i_arg2
        ints[i_out] = (arg1 + arg2) if opcode == 1 else (arg1 * arg2)
        index += 4
    elif opcode == 3:
        i_out = ints[index+1]
        ints[i_out] = inputs.pop()
        index += 2
    elif opcode == 4:
        i_arg1 = ints[index+1]
        arg1 = ints[i_arg1] if modes[0] == 0 else i_arg1
        outputs.append(arg1)
        index += 2

print(outputs)

# --- Part Two ---
ints = [int(x) for x in lines[0].split(',')]
inputs = [5]
outputs = []

index = 0
while ints[index] != 99:
    opcode = ints[index]
    modes = [int(s) for s in ('000' + str(opcode))[-3::-1]]
    opcode = int(str(opcode)[-1])
    if opcode == 1 or opcode == 2:
        i_arg1, i_arg2, i_out = ints[index+1:index+4]
        arg1 = ints[i_arg1] if modes[0] == 0 else i_arg1
        arg2 = ints[i_arg2] if modes[1] == 0 else i_arg2
        ints[i_out] = (arg1 + arg2) if opcode == 1 else (arg1 * arg2)
        index += 4
    elif opcode == 3:
        i_out = ints[index+1]
        ints[i_out] = inputs.pop()
        index += 2
    elif opcode == 4:
        i_arg1 = ints[index+1]
        arg1 = ints[i_arg1] if modes[0] == 0 else i_arg1
        outputs.append(arg1)
        index += 2
    elif opcode == 5 or opcode == 6:
        i_arg1, i_arg2 = ints[index+1:index+3]
        arg1 = ints[i_arg1] if modes[0] == 0 else i_arg1
        arg2 = ints[i_arg2] if modes[1] == 0 else i_arg2
        if (arg1 != 0) if opcode == 5 else (arg1 == 0):
            index = arg2
        else:
            index += 3
    elif opcode == 7 or opcode == 8:
        i_arg1, i_arg2, i_out = ints[index+1:index+4]
        arg1 = ints[i_arg1] if modes[0] == 0 else i_arg1
        arg2 = ints[i_arg2] if modes[1] == 0 else i_arg2
        if (arg1 < arg2) if opcode == 7 else (arg1 == arg2):
            ints[i_out] = 1
        else:
            ints[i_out] = 0
        index += 4

print(outputs)