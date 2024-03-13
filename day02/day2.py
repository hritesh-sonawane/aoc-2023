#!/usr/bin/env python3

from functools import reduce
import sys
from collections import defaultdict

target = defaultdict(int, {"red": 12, "blue": 14, "green": 13})

with open(sys.argv[1], 'r') as f:
    lines = [l.strip() for l in f.readlines()]

###
part1 = 0
part2 = 0

for line in lines:
    game_str, pull_str = line.split(": ")
    game_id = int(game_str.split(" ")[-1])
    p1_game_valid = True
    p2_set = defaultdict(int)

    for pull in pull_str.split("; "):
        for color_str in pull.split(", "):
            num_str, color = color_str.split(" ")
            num = int(num_str)

            if target[color] < num:
                p1_game_valid = False
            p2_set[color] = max(p2_set[color], num)
    
    if p1_game_valid:
        part1 += game_id
    
    part2 += reduce(lambda x, y: x * y, p2_set.values(), 1)


print(f'Part 1: {part1}')
print(f'Part 2: {part2}')