# Author: Kaustav Ghosh
# Problem: Magnetic Force Between Two Balls
# Approach: If some minimum spacing is achievable then every smaller spacing is too, so binary search the spacing. Testing one is greedy on the sorted baskets: always place the next ball in the first basket far enough from the last placed, which fits the most balls possible for that spacing

class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        baskets = sorted(position)

        def fits(gap):
            placed = 1
            last = baskets[0]
            for spot in baskets[1:]:
                if spot - last >= gap:
                    placed += 1
                    last = spot
            return placed >= m

        low, high = 1, baskets[-1] - baskets[0]
        while low < high:
            mid = (low + high + 1) // 2
            if fits(mid):
                low = mid
            else:
                high = mid - 1
        return low
