# Author: Kaustav Ghosh
# Problem: Count Largest Group
# Approach: Group numbers by digit sum, count largest groups

from collections import Counter

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        groups = Counter()
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            groups[digit_sum] += 1
        max_size = max(groups.values())
        return sum(1 for v in groups.values() if v == max_size)
