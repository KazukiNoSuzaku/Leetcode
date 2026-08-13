# Author: Kaustav Ghosh
# Problem: Average Height of Buildings in Each Segment
# Approach: Sweep across all start/end coordinates accumulating total height and building count as deltas. Between consecutive coordinates both stay constant, so emit the floored average where any building covers the stretch, merging contiguous segments that share the same average

from collections import defaultdict

class Solution(object):
    def averageHeightOfBuildings(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        delta_h = defaultdict(int)
        delta_c = defaultdict(int)
        for start, end, height in buildings:
            delta_h[start] += height
            delta_c[start] += 1
            delta_h[end] -= height
            delta_c[end] -= 1

        positions = sorted(set(delta_h))
        result = []
        cur_h = cur_c = 0
        prev = None
        for pos in positions:
            if prev is not None and cur_c > 0:
                avg = cur_h // cur_c
                if result and result[-1][1] == prev and result[-1][2] == avg:
                    result[-1][1] = pos
                else:
                    result.append([prev, pos, avg])
            cur_h += delta_h[pos]
            cur_c += delta_c[pos]
            prev = pos
        return result
