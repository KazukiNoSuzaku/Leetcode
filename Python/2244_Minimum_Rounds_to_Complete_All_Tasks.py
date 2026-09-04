# Author: Kaustav Ghosh
# Problem: Minimum Rounds to Complete All Tasks
# Approach: Tasks of each difficulty are cleared in rounds of two or three. A single leftover task is impossible (return -1). For a count c, the fewest rounds is ceil(c/3), since using as many triples as possible and filling the remainder with a pair or triple is optimal. Sum over all difficulties

from collections import Counter


class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        rounds = 0
        for c in Counter(tasks).values():
            if c == 1:
                return -1
            rounds += (c + 2) // 3
        return rounds
