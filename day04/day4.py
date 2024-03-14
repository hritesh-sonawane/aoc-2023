#!/usr/bin/env python3

import sys

def score_card(card):
    _, numbers = card.split(": ")
    win_str, numbers_str = numbers.split(" | ")
    wins = [int(x) for x in win_str.split(" ") if x]
    nums = [int(x) for x in numbers_str.split(" ") if x]

    return len([x for x in nums if x in wins])


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    
part1 = sum(int(pow(2, score_card(l) - 1)) for l in lines)
print(f'Part 1: {part1}')

cards = {i: 1 for i in range(len(lines))}

for i, card in enumerate(lines):
    num = score_card(card)

    for j in range(i + 1, i + 1 + num):
        cards[j] += cards[i]

part2 = sum(cards.values())
print(f'Part 2: {part2}')