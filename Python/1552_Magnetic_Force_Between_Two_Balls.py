# Author: Kaustav Ghosh
# Problem: 1552 - Magnetic Force Between Two Balls
# Approach: Binary search on minimum distance between any two balls

class Solution(object):
    def maxMinDist(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()

        def can_place(min_dist):
            count = 1
            last = position[0]
            for pos in position[1:]:
                if pos - last >= min_dist:
                    count += 1
                    last = pos
                    if count == m:
                        return True
            return count >= m

        lo, hi = 1, position[-1] - position[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_place(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
