# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: For each interval, subtract the removal range

class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        result = []
        lo, hi = toBeRemoved
        for start, end in intervals:
            if end <= lo or start >= hi:
                result.append([start, end])
            else:
                if start < lo:
                    result.append([start, lo])
                if end > hi:
                    result.append([hi, end])
        return result
