#!/usr/bin/env python3

import sys

def get_next(seq):
    if all(x == 0 for x in seq):
        return 0
    
    diff = [x2 - x1 for x1, x2 in zip(seq, seq[1:])] # zip: 1,2 => 2,3 => 3,4 ,..
    return seq[-1] + get_next(diff)

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    
part1 = sum(get_next(list(map(int, l.split()))) for l in lines)
print(f'Part 1: {part1}')

part2 = sum(get_next(list(map(int, l.split()[::-1]))) for l in lines)
print(f'Part 2: {part2}')