#!/usr/bin/env python3

import sys

def hash_string(s):
    hash_value = 0
    for char in s:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    
    return hash_value

with open(sys.argv[1], "r") as f:
    words = f.read().strip().split(",")

part1 = sum(hash_string(word) for word in words)
print(f"Part 1: {part1}")

boxes = [[] for _ in range(256)]
focal_len_map = {}

for instruction in words:
    if "=" in instruction:
        label, value = instruction.split("=")
        if label not in boxes[hash_string(label)]:
            boxes[hash_string(label)].append(label) 
        focal_len_map[label] = int(value)
    
    elif instruction.endswith("-"):
        label = instruction.strip("-")
        
        if label in boxes[hash_string(label)]:
            boxes[hash_string(label)].remove(label)
    else:
        assert False

part2 = 0
for box_number, box in enumerate(boxes, 1):
    for label_number, label in enumerate(box, 1):
        part2 += box_number * label_number * focal_len_map[label]

print(f"Part 2: {part2}")