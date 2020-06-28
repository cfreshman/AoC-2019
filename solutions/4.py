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
lower, upper = map(int, lines[0].split('-'))
num_passwords = 0
for i in range(lower, upper+1):
    s = str(i)
    has_decrease = False
    has_double = False
    for j in range(len(s)-1):
        if s[j] > s[j+1]:
            has_decrease = True
            break
        elif s[j] == s[j+1]:
            has_double = True
    if not has_decrease and has_double:
        num_passwords += 1

print(num_passwords)

# --- Part Two ---
num_passwords = 0
for i in range(lower, upper+1):
    s = str(i)
    has_decrease = False
    has_double = False
    for j in range(len(s)-1):
        if s[j] > s[j+1]:
            has_decrease = True
            break
        elif s[j] == s[j+1]:
            if (j-1 == -1 or s[j-1] != s[j]) and (j+2 == len(s) or s[j+2] != s[j]):
                has_double = True
    if not has_decrease and has_double:
        num_passwords += 1

print(num_passwords)