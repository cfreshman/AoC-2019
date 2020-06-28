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
def intcode(ints, inputs):
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
            ints[i_out] = inputs.pop(0)
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
    return outputs

base_ints = [int(x) for x in lines[0].split(',')]
max_output = -math.inf
max_setting = []
for setting in itertools.permutations(range(5)):
    outputs = [0]
    for amp in range(5):
        inputs = [setting[amp], outputs[0]]
        ints = base_ints.copy()
        outputs = intcode(ints, inputs)

    if outputs[0] > max_output:
        max_output = outputs[0]
        max_setting = setting

print(max_output, max_setting)

# --- Part Two ---
class Intcode:
    def __init__(self, ints):
        self.ints = ints.copy()
        self.i = 0
        self.inputs = []
        self.outputs = []
        self.paused = False
        self.halted = False

    def addInputs(self, inputs):
        if inputs:
            self.paused = False
            self.inputs.extend(inputs)

    def popOutputs(self):
        outputs = self.outputs
        self.outputs = []
        return outputs

    def run(self):
        while self.ints[self.i] != 99:
            self.paused = False
            opcode = self.ints[self.i]
            modes = [int(s) for s in ('000' + str(opcode))[-3::-1]]
            opcode = int(str(opcode)[-1])
            if opcode == 1 or opcode == 2:
                i_arg1, i_arg2, i_out = self.ints[self.i+1:self.i+4]
                arg1 = self.ints[i_arg1] if modes[0] == 0 else i_arg1
                arg2 = self.ints[i_arg2] if modes[1] == 0 else i_arg2
                self.ints[i_out] = (arg1 + arg2) if opcode == 1 else (arg1 * arg2)
                self.i += 4
            elif opcode == 3:
                if not self.inputs:
                    self.paused = True
                    return
                i_out = self.ints[self.i+1]
                self.ints[i_out] = self.inputs.pop(0)
                self.i += 2
            elif opcode == 4:
                i_arg1 = self.ints[self.i+1]
                arg1 = self.ints[i_arg1] if modes[0] == 0 else i_arg1
                self.outputs.append(arg1)
                self.i += 2
            elif opcode == 5 or opcode == 6:
                i_arg1, i_arg2 = self.ints[self.i+1:self.i+3]
                arg1 = self.ints[i_arg1] if modes[0] == 0 else i_arg1
                arg2 = self.ints[i_arg2] if modes[1] == 0 else i_arg2
                if (arg1 != 0) if opcode == 5 else (arg1 == 0):
                    self.i = arg2
                else:
                    self.i += 3
            elif opcode == 7 or opcode == 8:
                i_arg1, i_arg2, i_out = self.ints[self.i+1:self.i+4]
                arg1 = self.ints[i_arg1] if modes[0] == 0 else i_arg1
                arg2 = self.ints[i_arg2] if modes[1] == 0 else i_arg2
                if (arg1 < arg2) if opcode == 7 else (arg1 == arg2):
                    self.ints[i_out] = 1
                else:
                    self.ints[i_out] = 0
                self.i += 4
        self.halted = True

ints = [int(x) for x in lines[0].split(',')]
max_output = -math.inf
max_setting = []
for setting in itertools.permutations(range(5, 10)):
    outputs = [0]
    amps = []
    for i in range(5):
        amps.append(Intcode(ints))
        amps[i].addInputs([setting[i]])

    amps[0].addInputs([0])
    i = 0
    while True:
        amps[i].run()
        if i == 4 and amps[i].halted:
            break
        amps[(i+1)%5].addInputs(amps[i].popOutputs())
        i = (i+1)%5

    output = amps[4].outputs[0]
    if output > max_output:
        max_output = output
        max_setting = setting

print(max_output, max_setting)