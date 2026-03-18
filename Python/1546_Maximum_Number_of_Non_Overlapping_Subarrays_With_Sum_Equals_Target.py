# Author: Kaustav Ghosh
# Problem: 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
# Approach: Greedy prefix sum - extend window when target found, reset

class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        seen = {0}
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            if prefix - target in seen:
                result += 1
                seen = {0}
                prefix = 0
            else:
                seen.add(prefix)
        return result
