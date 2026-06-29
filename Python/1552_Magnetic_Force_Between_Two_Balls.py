# Author: Kaustav Ghosh
# Problem: Magnetic Force Between Two Balls
# Approach: Binary search the answer (minimum gap); greedily place balls left to right and check if m of them fit with that gap

class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()

        def can_place(force):
            count = 1
            last = position[0]
            for p in position[1:]:
                if p - last >= force:
                    count += 1
                    last = p
                    if count >= m:
                        return True
            return count >= m

        lo, hi = 1, position[-1] - position[0]
        best = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return best
