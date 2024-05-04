#!/usr/bin/env python3

import sys


class Grid:
    def __init__(self, initial_grid):
        self.grid = initial_grid
        self.rotate_counter_clockwise()

    def rotate_counter_clockwise(self):
        self.grid = tuple(map("".join, zip(*self.grid)))[::-1]

    def rotate_clockwise(self):
        for _ in range(3):
            self.rotate_counter_clockwise()

    def print_grid(self):
        print("\n".join(self.grid))
        print()

    def tilt_north(self):
        self.grid = tuple(
            "#".join(["".join(sorted(s, reverse=True)) for s in row.split("#")])
            for row in self.grid
        )

    def tilt_cycle(self):
        for _ in range(4):
            self.tilt_north()
            self.rotate_clockwise()

    def tilt_cycles(self, cycles):
        states = [self.grid]
        count = 0
        while count < cycles:
            self.tilt_cycle()
            count += 1
            if self.grid in states:
                break
            states.append(self.grid)
        if count == cycles:
            return
        first_seen = states.index(self.grid)
        cycle_length = count - first_seen
        self.grid = states[(cycles - first_seen) % cycle_length + first_seen]

    def total_load(self):
        total = sum(
            len(self.grid[0]) - i
            for row in self.grid
            for i, ch in enumerate(row)
            if ch == "O"
        )
        return total


with open(sys.argv[1], "r") as f:
    grid_lines = [l.strip() for l in f.readlines()]

initial_grid = grid_lines
grid = Grid(initial_grid)
grid.tilt_north()
part1 = grid.total_load()
print(f"Part 1: {part1}")

grid2 = Grid(initial_grid)
grid2.tilt_cycles(1000000000)
part2 = grid2.total_load()
print(f"Part 2: {part2}")