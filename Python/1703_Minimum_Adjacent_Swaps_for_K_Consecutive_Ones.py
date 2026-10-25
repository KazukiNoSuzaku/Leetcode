# Author: Kaustav Ghosh
# Problem: Minimum Adjacent Swaps for K Consecutive Ones
# Approach: Only the ones matter, and they keep their relative order under adjacent swaps, so the choice is which k consecutive ones to gather and the cost is how far each must travel. Gathering them into consecutive cells means the i-th chosen one ends up i places after the first, so subtracting each one's rank from its position removes that built-in spacing and turns the problem into collecting k values at a single point, where the cheapest meeting point is their median. With the positions adjusted that way, a window's cost is the distance from its middle element, which a prefix total evaluates in constant time, so every window is priced in one sweep.

class Solution(object):
    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Position minus rank: gathering becomes meeting at one point.
        adjusted = [position - rank
                    for rank, position in enumerate(i for i, v in enumerate(nums) if v)]
        m = len(adjusted)
        prefix = [0] * (m + 1)
        for i, value in enumerate(adjusted):
            prefix[i + 1] = prefix[i] + value

        best = None
        half = k // 2
        for left in range(m - k + 1):
            right = left + k - 1
            middle = left + half
            pivot = adjusted[middle]
            below = pivot * (middle - left) - (prefix[middle] - prefix[left])
            above = (prefix[right + 1] - prefix[middle + 1]) - pivot * (right - middle)
            cost = below + above
            if best is None or cost < best:
                best = cost
        return best
