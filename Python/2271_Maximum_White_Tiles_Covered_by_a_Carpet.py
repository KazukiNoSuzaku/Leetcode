# Author: Kaustav Ghosh
# Problem: 2271. Maximum White Tiles Covered by a Carpet
# URL: https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/
# Difficulty: Medium
#
# Approach:
# Sort tiles by start. Use a sliding window with prefix sums of tile lengths.
# For each carpet placement starting at a tile's left edge, binary search
# for the rightmost tile fully covered, then add partial coverage of the next.

import bisect

class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int
        """
        tiles.sort()
        n = len(tiles)
        starts = [t[0] for t in tiles]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (tiles[i][1] - tiles[i][0] + 1)

        best = 0
        for i in range(n):
            carpet_end = tiles[i][0] + carpetLen - 1
            j = bisect.bisect_right(starts, carpet_end) - 1
            covered = prefix[j] - prefix[i]
            # Add partial coverage of tiles[j] if carpet_end falls within it
            partial = min(carpet_end, tiles[j][1]) - tiles[j][0] + 1
            covered += max(0, partial)
            best = max(best, covered)
        return best
