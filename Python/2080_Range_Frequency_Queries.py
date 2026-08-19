# Author: Kaustav Ghosh
# Problem: Range Frequency Queries
# Approach: Store the sorted list of indices where each value occurs. A range query counts how many of that value's indices fall in [left, right] via two binary searches

import bisect
from collections import defaultdict

class RangeFreqQuery(object):
    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.positions = defaultdict(list)
        for i, v in enumerate(arr):
            self.positions[v].append(i)

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        idx = self.positions.get(value)
        if not idx:
            return 0
        return bisect.bisect_right(idx, right) - bisect.bisect_left(idx, left)
