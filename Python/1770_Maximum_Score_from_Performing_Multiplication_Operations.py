# Author: Kaustav Ghosh
# Problem: Maximum Score from Performing Multiplication Operations
# Approach: After i operations of which l came from the front, the untouched part of nums is fully determined: it starts at index l and ends at index n - 1 - (i - l). The state is therefore just the pair (i, l) and never the array itself, which keeps the table at m^2 entries even though nums can hold 100000 numbers. Working backwards from the last operation, each state takes the better of consuming nums[l] or the matching element from the tail, so one rolling row of length m + 1 is enough.

class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        n, m = len(nums), len(multipliers)
        after = [0] * (m + 1)
        for operation in range(m - 1, -1, -1):
            factor = multipliers[operation]
            current = [0] * (m + 1)
            for taken_left in range(operation, -1, -1):
                right = n - 1 - (operation - taken_left)
                current[taken_left] = max(factor * nums[taken_left] + after[taken_left + 1],
                                          factor * nums[right] + after[taken_left])
            after = current
        return after[0]
