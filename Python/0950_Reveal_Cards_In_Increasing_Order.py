# Reorder deck so that revealing cards in the zigzag sequence gives sorted order.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        deck.sort()
        index = deque(range(n))
        res = [0] * n
        for card in deck:
            res[index.popleft()] = card
            if index: index.append(index.popleft())
        return res
