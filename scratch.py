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
print(sum(int(x)//3 - 2 for x in lines))


# --- Part Two ---
def recurseFuel(x):
    fuelNeeded = x//3 - 2
    if fuelNeeded < 1:
        return 0
    else:
        return fuelNeeded + recurseFuel(fuelNeeded)

print(sum(recurseFuel(int(x)) for x in lines))