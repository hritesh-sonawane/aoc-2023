#!/usr/bin/env python3

import sys
from functools import cache


@cache
def get_combinations(springs, nums):
    total = 0

    if len(springs) == 0:
        if len(nums) == 0:
            return 1
        return 0

    if len(nums) == 0:
        if "#" in springs:
            return 0
        return 1

    if len(springs) < sum(nums) + len(nums) - 1:
        return 0

    if springs[0] in ".?":
        total += get_combinations(springs[1:], nums)

    n = nums[0]
    if (
        springs[0] in "#?"
        and "." not in springs[:n]
        and (len(springs) == n or springs[n] in ".?")
    ):
        total += get_combinations(springs[n + 1 :], nums[1:])

    return total


def solve(lines, fold=1):
    count = 0
    for line in lines:
        springs, nums = line.split(" ")
        springs = "?".join([springs] * fold)
        nums = tuple(int(n) for n in nums.split(",")) * fold
        count += get_combinations(springs, nums)
    return count


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

part1 = solve(lines)
print(f"Part 1: {part1}")

part2 = solve(lines, fold=5)
print(f"Part 2: {part2}")