# Author: Kaustav Ghosh
# Problem: Maximum Erasure Value
# Approach: Sliding window with a set of the current elements; shrink from the left on a duplicate, tracking the best window sum

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        left = 0
        cur = 0
        best = 0
        for x in nums:
            while x in seen:
                seen.remove(nums[left])
                cur -= nums[left]
                left += 1
            seen.add(x)
            cur += x
            best = max(best, cur)
        return best
