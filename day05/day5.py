#!/usr/bin/env python3

import sys
from typing import Dict, Optional, List


class Range:
    def __init__(self, source, length):
        self.start = source
        self.end = source + length

    def __repr__(self):
        return f"<Range [{self.start}-{self.end}]"


class Translation:
    def __init__(self, dest, source, length):
        self.start = source
        self.end = source + length
        self.offset = source - dest

    def trans(self, num):
        if self.start <= num < self.end:
            return num - self.offset
        return None


class Map:
    def __init__(self, lines):
        self.translations = []
        for line in lines.split("\n")[1:]:
            dest, source, length = map(int, line.split(" "))
            self.translations.append(Translation(dest, source, length))

    def translate(self, num):
        for t in self.translations:
            if next_num := t.trans(num): # lol, python has ":=" (walrus operator)
                return next_num
        return num

    def translate_range(self, seed_ranges):
        srs = [r for r in seed_ranges]
        res_ranges = []
        while srs:
            seed_range = srs.pop()
            for trans in self.translations:
                over_start = max(trans.start, seed_range.start)
                over_end = min(trans.end, seed_range.end)
                if over_start < over_end:
                    res_ranges.append(
                        Range(over_start - trans.offset, over_end - over_start)
                    )
                    if seed_range.start < over_start:
                        srs.append(
                            Range(seed_range.start, over_start - seed_range.start)
                        )
                    if over_end < seed_range.end:
                        srs.append(Range(over_end, seed_range.end - over_end))
                    break
            else:
                res_ranges.append(seed_range)
        return res_ranges


class Almanac:
    def __init__(self, puz_input):
        blocks = puz_input.split("\n\n")
        self.seeds = list(map(int, blocks[0].split(": ")[1].split(" ")))
        self.seed_ranges = [
            Range(start, length) for start, length in zip(*(iter(self.seeds),) * 2)
        ]
        self.maps = [Map(block) for block in blocks[1:]]

    def solve(self):
        results = {}
        for seed in self.seeds:
            res = seed
            for m in self.maps:
                res = m.translate(res)
            results[seed] = res
        return results

    def solve2(self):
        seed_ranges = [r for r in self.seed_ranges]
        for m in self.maps:
            seed_ranges = m.translate_range(seed_ranges)
        return seed_ranges


with open(sys.argv[1], "r") as f:
    puz_input = f.read().strip()


almanac = Almanac(puz_input)
part1 = min(almanac.solve().values())
print(f"Part 1: {part1}")

part2 = min(r.start for r in almanac.solve2())
print(f"Part 2: {part2}")