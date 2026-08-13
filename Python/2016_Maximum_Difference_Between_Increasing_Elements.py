# Author: Kaustav Ghosh
# Problem: Maximum Difference Between Increasing Elements
# Approach: Track the minimum value seen so far; for each later element the best difference is value minus that minimum. Keep the largest positive difference, or -1 if none

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_so_far = nums[0]
        best = -1
        for v in nums[1:]:
            if v > min_so_far:
                best = max(best, v - min_so_far)
            else:
                min_so_far = v
        return best
