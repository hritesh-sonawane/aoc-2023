#!/usr/bin/env python3

import math
import sys


def get_steps(start):
    steps = 0
    pos = start

    while not pos.endswith("Z"):
        dir = directions[steps % len_dirs]
        pos = node_map[pos][dir]
        steps += 1

    return steps


with open(sys.argv[1], "r") as f:
    directions_str, _, *nodes = (l.strip() for l in f.readlines())

directions = [int(c == "R") for c in directions_str]
len_dirs = len(directions)
node_map = {}
startings = []

for line in nodes:
    key, targets = line.split(" = ")
    if key.endswith("A"):
        startings.append(key)
    node_map[key] = targets.strip("()").split(", ")


part1 = get_steps("AAA")
print(f"Part 1: {part1}")

step_counts = [get_steps(start) for start in startings]

part2 = math.lcm(*step_counts)
print(f"Part 2: {part2}")