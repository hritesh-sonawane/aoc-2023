#!/usr/bin/env python3

import sys


def find_mirror(block, diffs=0):
    for i in range(1, len(block)):
        above = block[:i][::-1]
        below = block[i:]
        if (
            sum(
                sum(0 if a == b else 1 for a, b in zip(ar, br))
                for ar, br in zip(above, below)
            )
            == diffs
        ):
            return i
    return 0


def solve(blocks, diffs=0):
    total = 0
    for block in blocks:
        block = block.splitlines()
        total += find_mirror(block, diffs=diffs) * 100
        total += find_mirror(list(zip(*block)), diffs=diffs)
    return total


with open(sys.argv[1], "r") as f:
    blocks = f.read().split("\n\n")

part1 = solve(blocks)
print(f"Part 1: {part1}")

part2 = solve(blocks, diffs=1)
print(f"Part 2: {part2}")