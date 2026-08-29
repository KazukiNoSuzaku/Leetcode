# Author: Kaustav Ghosh
# Problem: Maximum AND Sum of Array
# Approach: Each slot accepts at most two numbers, so the state is how many numbers each slot holds (0,1,2) encoded per slot. Place numbers in order; the count placed equals the total occupancy. DP over slot-occupancy states, choosing which slot to place the next number into to maximize the AND sum

from functools import lru_cache

class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        """
        :type nums: List[int]
        :type numSlots: int
        :rtype: int
        """
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(slots):
            placed = sum(slots)
            if placed == n:
                return 0
            num = nums[placed]
            best = 0
            for j in range(numSlots):
                if slots[j] < 2:
                    new = slots[:j] + (slots[j] + 1,) + slots[j + 1:]
                    best = max(best, (num & (j + 1)) + dp(new))
            return best

        return dp((0,) * numSlots)
