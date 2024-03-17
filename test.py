#!/usr/bin/env python3
import math
import sys


def solve_quad(t, d):
    a = -1
    b = t
    c = -d
    root1 = math.ceil((-b + pow(b * b - (4 * a * c), 0.5)) / (2 * a) + 0.00000000000001)
    root2 = math.floor(
        (-b - pow(b * b - (4 * a * c), 0.5)) / (2 * a) - 0.00000000000001
    )
    return root2 - root1 + 1


def count_solutions(t, d):
    return sum(1 for i in range(t) if (t - i) * i > d)


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

times, dists = [list(map(int, l.split(":")[1].strip().split())) for l in lines]

"""
Time:      7  15   30
Distance:  9  40  200

(t - b) * b > d
-b^2 + t*b - d > 0
"""
# part1 = math.prod(solve_quad(t,d) for t,d in zip(times, dists))
part1 = math.prod(count_solutions(t, d) for t, d in zip(times, dists))
print(f"Part 1: {part1}")

# part2 = solve_quad(int(''.join(str(t) for t in times)), int(''.join(str(d) for d in dists)))
part2 = count_solutions(
    int("".join(str(t) for t in times)), int("".join(str(d) for d in dists))
)
print(f"Part 2: {part2}")
