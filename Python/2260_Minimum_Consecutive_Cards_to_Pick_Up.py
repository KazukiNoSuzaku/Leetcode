# Author: Kaustav Ghosh
# Problem: 2260. Minimum Consecutive Cards to Pick Up
# URL: https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
# Difficulty: Medium
#
# Approach:
# Track the last seen index of each card value. When a duplicate is found,
# the window size is current index - last index + 1. Track the minimum.

class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        last_seen = {}
        min_len = float('inf')
        for i, card in enumerate(cards):
            if card in last_seen:
                min_len = min(min_len, i - last_seen[card] + 1)
            last_seen[card] = i
        return min_len if min_len != float('inf') else -1
