#!/usr/bin/env python3

import sys


class HANDTYPE:
    HIGHCARD = 1
    PAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    FULLHOUSE = 5
    FOUROFAKIND = 6
    FIVEOFAKIND = 7


class Hand(object):
    def __init__(self, hand, bet, part2=False):
        self.hand = hand
        self.bet = int(bet)
        self.hand_type = self.get_hand_type(part2)
        self.card_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
        if part2:
            self.card_map["J"] = "0"

    def __repr__(self):
        return "<Hand {} [{}]: {}>".format(self.hand, self.hand_type.name, self.bet)

    def __eq__(self, other):
        return self.hand == other.hand

    def __gt__(self, other):
        if self.hand_type == other.hand_type:
            self_cards = [self.card_map.get(c, c) for c in self.hand]
            other_cards = [self.card_map.get(c, c) for c in other.hand]
            return self_cards > other_cards
        return self.hand_type > other.hand_type

    def get_hand_type(self, part2):
        if not part2:
            return self.get_hand_rank(self.hand)
        return max([self.get_hand_rank(h) for h in self.replace_wilds(self.hand)])

    @staticmethod
    def replace_wilds(hand):
        if not hand:
            return [""]
        return [
            a + b
            for a in ("23456789TQKA" if hand[0] == "J" else hand[0])
            for b in Hand.replace_wilds(hand[1:])
        ]

    @staticmethod
    def get_hand_rank(hand):
        counts = [hand.count(c) for c in hand]
        if 5 in counts:
            return HANDTYPE.FIVEOFAKIND
        if 4 in counts:
            return HANDTYPE.FOUROFAKIND
        if 3 in counts:
            if 2 in counts:
                return HANDTYPE.FULLHOUSE
            return HANDTYPE.THREEOFAKIND
        if counts.count(2) == 4:
            return HANDTYPE.TWOPAIR
        if 2 in counts:
            return HANDTYPE.PAIR
        return HANDTYPE.HIGHCARD


def process_hands(lines, part2=False):
    hands = []
    for line in lines:
        hand, bet = line.split()
        hands.append(Hand(hand, bet, part2=part2))
    
    total_bet = 0
    for rank, hand in enumerate(sorted(hands), 1):
        total_bet += rank * hand.bet
    
    return total_bet

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

part1 = process_hands(lines)
print("Part 1: {}".format(part1))

part2 = process_hands(lines, part2=True)
print("Part 2: {}".format(part2))