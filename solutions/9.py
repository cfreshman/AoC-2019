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
class Intcode:
    def __init__(self, ints):
        self.ints = ints.copy()
        self.i = 0
        self.relative_base = 0
        self.inputs = []
        self.outputs = []
        self.paused = False
        self.halted = False

    def add_inputs(self, inputs):
        if inputs:
            self.paused = False
            self.inputs.extend(inputs)

    def pop_outputs(self):
        outputs = self.outputs
        self.outputs = []
        return outputs

    def get(self, i):
        return 0 if i >= len(self.ints) else self.ints[i]

    def set(self, i, value):
        if i >= len(self.ints):
            self.ints.extend([0] * (i - len(self.ints) + 1))
        self.ints[i] = value

    def getArg(self, arg, mode):
        if mode == 0: return self.get(arg)
        if mode == 1: return arg
        if mode == 2: return self.get(arg + self.relative_base)

    def getArgs(self, n_args, modes):
        return [self.getArg(self.get(self.i+1 + i), modes[i]) for i in range(n_args)]

    def getOut(self, out, mode):
        if mode == 0: return out
        if mode == 2: return out + self.relative_base

    def run(self):
        while self.get(self.i) != 99:
            self.paused = False
            opcode = self.get(self.i)
            modes = [int(s) for s in ('0000' + str(opcode))[-3::-1]]
            opcode = int(str(opcode)[-1])
            # add & mult
            if opcode == 1 or opcode == 2:
                arg1, arg2 = self.getArgs(2, modes)
                i_out = self.getOut(self.get(self.i + 3), modes[2])
                self.set(i_out, (arg1 + arg2) if opcode == 1 else (arg1 * arg2))
                self.i += 4
            # input
            elif opcode == 3:
                if not self.inputs:
                    self.paused = True
                    return
                i_out = self.getOut(self.get(self.i + 1), modes[0])
                self.set(i_out, self.inputs.pop(0))
                self.i += 2
            # output
            elif opcode == 4:
                arg1, = self.getArgs(1, modes)
                self.outputs.append(arg1)
                self.i += 2
            # jump-if-not-equal & jump-if-equal
            elif opcode == 5 or opcode == 6:
                arg1, arg2 = self.getArgs(2, modes)
                if (arg1 != 0) if opcode == 5 else (arg1 == 0):
                    self.i = arg2
                else:
                    self.i += 3
            # is-less-than & is-equal-to
            elif opcode == 7 or opcode == 8:
                arg1, arg2 = self.getArgs(2, modes)
                i_out = self.getOut(self.get(self.i + 3), modes[2])
                if (arg1 < arg2) if opcode == 7 else (arg1 == arg2):
                    self.set(i_out, 1)
                else:
                    self.set(i_out, 0)
                self.i += 4
            # adjust relative base
            elif opcode == 9:
                arg1, = self.getArgs(1, modes)
                self.relative_base += arg1
                self.i += 2
        self.halted = True

ints = [int(x) for x in lines[0].split(',')]
comp = Intcode(ints)
comp.add_inputs([1])
comp.run()
print(comp.outputs)

# --- Part Two ---
comp = Intcode(ints)
comp.add_inputs([2])
comp.run()
print(comp.outputs)