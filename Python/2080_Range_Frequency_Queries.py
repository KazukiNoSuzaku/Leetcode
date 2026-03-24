# Author: Kaustav Ghosh
# Problem 2080: Range Frequency Queries

from bisect import bisect_left, bisect_right
from collections import defaultdict

class RangeFreqQuery(object):
    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.positions = defaultdict(list)
        for i, val in enumerate(arr):
            self.positions[val].append(i)

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        if value not in self.positions:
            return 0
        pos = self.positions[value]
        lo = bisect_left(pos, left)
        hi = bisect_right(pos, right)
        return hi - lo
