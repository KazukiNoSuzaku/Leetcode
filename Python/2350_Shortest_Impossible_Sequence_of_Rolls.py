# Author: Kaustav Ghosh
# 2350. Shortest Impossible Sequence of Rolls
# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/
# Difficulty: Hard
#
# Greedy: scan rolls and collect a complete set of 1..k. Each time we complete
# a full set, we can form one more guaranteed prefix length. The answer is
# (number of complete sets found) + 1.

class Solution(object):
    def shortestSequence(self, rolls, k):
        """
        :type rolls: List[int]
        :type k: int
        :rtype: int
        """
        seen = set()
        complete_sets = 0
        for r in rolls:
            seen.add(r)
            if len(seen) == k:
                complete_sets += 1
                seen = set()
        return complete_sets + 1
