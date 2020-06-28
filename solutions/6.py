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
orbits = {}
for line in lines:
    orbit, orbiter = line.split(')')
    if orbit not in orbits:
        orbits[orbit] = []
    orbits[orbit].append(orbiter)

def count_orbits(o, length):
    n_orbits = length
    if o in orbits:
        n_orbits += sum(count_orbits(o, length+1) for o in orbits[o])
    return n_orbits

print(count_orbits('COM', 0))

# --- Part Two ---
Node = namedtuple('Node', 'self adj')
graph = {}
def build_graph(o, parent=None):
    adj = []
    if parent:
        adj.append(parent)
    if o in orbits:
        adj.extend(orbits[o])
        [build_graph(child, o) for child in orbits[o]]
    graph[o] = adj
build_graph('COM')

def bfs(graph, start, target):
    visited = set()
    frontier = {(start, (start,))}
    while frontier:
        name, path = frontier.pop()
        if name == target:
            return path
        visited.add(name)
        for v in graph[name]:
            if v not in visited:
                frontier.add((v, path + (v,)))

path = bfs(graph, 'YOU', 'SAN')
print(len(path) - 3)