#!/usr/bin/env python3

import math
import sys

def solve_quadratic(t, d):
    a = -1
    b = t
    c = -d

    root1 = math.ceil((-b + pow(b * b - (4 * a * c), 0.5)) / (2 * a) + 0.00000000000001)
    root2 = math.floor((-b - pow(b * b - (4 * a * c), 0.5)) / (2 * a) - 0.00000000000001)

    return root2 - root1 + 1

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

times, dists = [list(map(int, l.split(":")[1].strip().split())) for l in lines]
    
part1 = math.prod(solve_quadratic(t, d) for t, d in zip(times, dists))
print(f'Part 1: {part1}')

part2 = solve_quadratic(int("".join(str(t) for t in times)), int("".join(str(d) for d in dists)))
print(f'Part 2: {part2}')

# brute force lol
# def count_solutions(t, d):
#     return sum(1 for i in range(t) if (t - i) * i > d)

# part1 = math.prod(count_solutions(t, d) for t, d in zip(times, dists))
# print(f"Part 1: {part1}")

# part2 = count_solutions(
#     int("".join(str(t) for t in times)), int("".join(str(d) for d in dists))
# )
# print(f"Part 2: {part2}")