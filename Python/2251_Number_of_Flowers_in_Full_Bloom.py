# Author: Kaustav Ghosh
# Problem: 2251. Number of Flowers in Full Bloom
# URL: https://leetcode.com/problems/number-of-flowers-in-full-bloom/
# Difficulty: Hard
#
# Approach:
# Separate start and end times, sort both. For each person's arrival time,
# binary search to count how many flowers have started blooming and how
# many have finished. The difference gives flowers in bloom.

import bisect

class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        starts = sorted(s for s, e in flowers)
        ends = sorted(e for s, e in flowers)

        result = []
        for t in people:
            bloomed = bisect.bisect_right(starts, t)
            ended = bisect.bisect_left(ends, t)
            result.append(bloomed - ended)
        return result
