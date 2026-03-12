# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Binary search per color on sorted index lists

class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import bisect
        from collections import defaultdict
        color_indices = defaultdict(list)
        for i, c in enumerate(colors):
            color_indices[c].append(i)

        result = []
        for idx, color in queries:
            if color not in color_indices:
                result.append(-1)
                continue
            indices = color_indices[color]
            pos = bisect.bisect_left(indices, idx)
            dist = float('inf')
            if pos < len(indices):
                dist = min(dist, indices[pos] - idx)
            if pos > 0:
                dist = min(dist, idx - indices[pos - 1])
            result.append(dist)
        return result
