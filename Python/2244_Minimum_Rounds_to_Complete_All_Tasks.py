# Author: Kaustav Ghosh
# Problem: 2244. Minimum Rounds to Complete All Tasks
# URL: https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
# Difficulty: Medium
#
# Approach:
# Count frequency of each difficulty. If any frequency is 1, return -1.
# Otherwise, the minimum rounds for count c is ceil(c / 3).

from collections import Counter

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        counts = Counter(tasks)
        rounds = 0
        for c in counts.values():
            if c == 1:
                return -1
            rounds += (c + 2) // 3
        return rounds
