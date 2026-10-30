# Author: Kaustav Ghosh
# Problem: Minimum Limit of Balls in a Bag
# Approach: Whether a given ceiling is reachable only gets easier as the ceiling rises, so the smallest workable ceiling is found by binary search rather than by simulating splits. Testing a ceiling needs no search of its own: a bag of x balls must end up as bags of at most the ceiling each, which takes as many splits as there are whole ceilings in x minus one, since each split adds exactly one bag. Summing that over the bags and comparing against the allowance decides the ceiling in one pass. The search runs from one up to the largest bag, which always works by doing nothing.

class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        low, high = 1, max(nums)
        while low < high:
            ceiling = (low + high) // 2
            splits = 0
            for balls in nums:
                splits += (balls - 1) // ceiling
                if splits > maxOperations:
                    break
            if splits <= maxOperations:
                high = ceiling
            else:
                low = ceiling + 1
        return low
