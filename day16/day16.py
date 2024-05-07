#!/usr/bin/env python3

import sys
from collections import deque

def count_powered(row, col, drow, dcol):
    seen = set()
    queue = deque([(row, col, drow, dcol)])

    while queue:
        row, col, drow, dcol = queue.popleft()

        # move
        row += drow
        col += dcol

        if not (0 <= row < height and 0 <= col < width):
            continue

        # turn!
        next_directions = []
        
        match grid[row][col]:
            case "/":
                # 0, 1 <-> -1, 0   1, 0 <-> 0, -1
                next_directions.append((-dcol, -drow))
            case "\\":
                # 0, 1 <-> 1, 0    0, -1 <-> -1, 0
                next_directions.append((dcol, drow))
            case "|":
                if dcol == 0:
                    next_directions.append((drow, dcol))
                else:
                    next_directions.extend([(1, 0), (-1, 0)])
            case "-":
                if drow == 0:
                    next_directions.append((drow, dcol))
                else:
                    next_directions.extend([(0, 1), (0, -1)])
            case ".":
                next_directions.append((drow, dcol))
            case _:
                assert False, f"unknown char {grid[row][col]}"

        for drow, dcol in next_directions:
            if (row, col, drow, dcol) not in seen:
                seen.add((row, col, drow, dcol))
                queue.append((row, col, drow, dcol))

    return len(set((row, col) for row, col, _, _ in seen))


with open(sys.argv[1], "r") as f:
    grid = [line.strip() for line in f.readlines()]
    height = len(grid)
    width = len(grid[0])

part1 = count_powered(0, -1, 0, 1)
print(f"Part 1: {part1}")

part2 = 0
for r in range(height):
    part2 = max(part2, count_powered(r, -1, 0, 1))
    part2 = max(part2, count_powered(r, width, 0, -1))
for c in range(width):
    part2 = max(part2, count_powered(-1, c, 1, 0))
    part2 = max(part2, count_powered(height, c, -1, 0))

print(f"Part 2: {part2}")