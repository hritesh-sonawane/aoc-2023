#!/usr/bin/env python3

import sys
import re


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

###
part1 = 0

for line in lines:
    # digits = [c for c in line if c.isdigit()]
    digits = re.sub(r"\D", "", line)
    part1 += int(digits[0]) * 10 + int(digits[-1])

print(f"Part 1: {part1}")

###
part2 = 0

num_map = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

for line in lines:
    for i, v in num_map.items():
        line = line.replace(i, v)
    digits = re.sub(r"\D", "", line)
    part2 += int(digits[0]) * 10 + int(digits[-1])

print(f"Part 2: {part2}")
