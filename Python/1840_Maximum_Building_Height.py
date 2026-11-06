# Author: Kaustav Ghosh
# Problem: Maximum Building Height
# Approach: Heights may differ by at most one between neighbours, so a restriction limits not only its own building but everything near it, and the real cap at each restricted building is the smallest value reachable from any other restriction. Sweeping the sorted restrictions left to right and then right to left propagates those limits in both directions, after which each pair of neighbouring restrictions is independent. Between two of them the tallest building sits where the two slopes meet, which is half the sum of their heights and their distance rounded down, and the stretch after the last restriction is free to rise all the way to the end. The first building is handled by entering it as a restriction of height zero, so it needs no special case.

class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        # Copied so the sweeps below cannot lower the caller's own restrictions.
        limits = sorted([list(limit) for limit in restrictions] + [[1, 0]])

        for i in range(1, len(limits)):
            limits[i][1] = min(limits[i][1], limits[i - 1][1] + limits[i][0] - limits[i - 1][0])
        for i in range(len(limits) - 2, -1, -1):
            limits[i][1] = min(limits[i][1], limits[i + 1][1] + limits[i + 1][0] - limits[i][0])

        tallest = 0
        for i in range(1, len(limits)):
            left_id, left_height = limits[i - 1]
            right_id, right_height = limits[i]
            peak = (left_height + right_height + right_id - left_id) // 2
            if peak > tallest:
                tallest = peak

        last_id, last_height = limits[-1]
        if last_id < n:
            tallest = max(tallest, last_height + n - last_id)
        return tallest
