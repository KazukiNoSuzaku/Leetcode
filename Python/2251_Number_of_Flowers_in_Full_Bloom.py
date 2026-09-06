# Author: Kaustav Ghosh
# Problem: Number of Flowers in Full Bloom
# Approach: A flower [s, e] is in bloom at time t when s <= t <= e. The count at t equals (flowers that have started by t) minus (flowers that have already ended before t). Sort the start and end times separately; for each person's time, binary search how many starts are <= t and how many ends are < t

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
        res = []
        for t in people:
            started = bisect.bisect_right(starts, t)
            ended = bisect.bisect_left(ends, t)
            res.append(started - ended)
        return res
