# Author: Kaustav Ghosh
# Problem: Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
# Approach: Track running prefix sums in a set; when prefix-target is seen, greedily count a subarray and reset the set to forbid overlap

class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        seen = {0}
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            if prefix - target in seen:
                count += 1
                # reset to prevent the next subarray from overlapping this one
                seen = {0}
                prefix = 0
            else:
                seen.add(prefix)
        return count
