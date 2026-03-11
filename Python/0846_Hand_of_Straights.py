# Check if a hand of cards can be divided into groups of W consecutive cards.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize: return False
        count = Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                n = count[card]
                for i in range(groupSize):
                    if count[card + i] < n: return False
                    count[card + i] -= n
        return True
