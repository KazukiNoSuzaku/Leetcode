# Author: Kaustav Ghosh
# Problem: Maximum White Tiles Covered by a Carpet
# Approach: An optimal carpet always starts at the left edge of some white-tile interval. Sort intervals and build a prefix sum of tile counts. For each interval as the start, the carpet covers up to start+len-1; binary search the interval containing that right end, add the fully covered tiles and the partial coverage of the last interval

import bisect


class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int
        """
        tiles.sort()
        starts = [t[0] for t in tiles]
        n = len(tiles)
        # prefix[i] = total white tiles in tiles[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (tiles[i][1] - tiles[i][0] + 1)

        best = 0
        for i in range(n):
            left = tiles[i][0]
            right_end = left + carpetLen - 1
            # find last interval whose start <= right_end
            j = bisect.bisect_right(starts, right_end) - 1
            # fully covered intervals i..j-1, plus partial of j
            covered = prefix[j] - prefix[i]
            partial = min(tiles[j][1], right_end) - tiles[j][0] + 1
            best = max(best, covered + partial)
        return best
