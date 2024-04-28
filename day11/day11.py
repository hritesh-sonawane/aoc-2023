#!/usr/bin/env python3

import sys
from itertools import combinations


def get_dist(g1, g2, space_dist=2):
    dist = 0
    for r in range(min(g1[0], g2[0]), max(g1[0], g2[0])):
        dist += space_dist if r in empty_rows else 1
    for c in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
        dist += space_dist if c in empty_cols else 1
    return dist


with open(sys.argv[1], "r") as f:
    grid = [l.strip() for l in f.readlines()]

galaxies = [
    (r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "#"
]

empty_rows = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)]
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]

part1 = sum(get_dist(g1, g2) for g1, g2 in combinations(galaxies, 2))
print(f"Part 1: {part1}")

part2 = sum(get_dist(g1, g2, 1000000) for g1, g2 in combinations(galaxies, 2))
print(f"Part 2: {part2}")