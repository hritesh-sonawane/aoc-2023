#!/usr/bin/env python3

import sys


def int_from_coord(r, c):
    dc = 0
    while c + dc + 1 < len(lines[0]) and lines[r][c + dc + 1].isdigit():
        dc += 1
    
    return int(lines[r][c: c + dc + 1])

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]

p1_numbers = set()
part2 = 0

for r, row in enumerate(lines):
    for c, char in enumerate(row):
        if char.isdigit() or char == ".":
            continue

        adj_nums = set()
        for rr in [r + 1, r, r - 1]:
            for cc in [c - 1, c, c + 1]:
                if rr < 0 or rr > len(lines) or cc < 0 or rr > len(lines[0]):
                    continue
                if lines[rr][cc].isdigit():
                    dc = 0
                    while lines[rr][cc + dc - 1].isdigit():
                        dc -= 1
                    
                    p1_numbers.add((rr, cc + dc))
                    if char == "*":
                        adj_nums.add((rr, cc + dc))

        if len(adj_nums) > 2:
            assert False

        if len(adj_nums) == 2:
            num1 = int_from_coord(*adj_nums.pop())
            num2 = int_from_coord(*adj_nums.pop())

            part2 += num1 * num2
    
part1 = 0
for r, c in p1_numbers:
    part1 += int_from_coord(r, c)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')