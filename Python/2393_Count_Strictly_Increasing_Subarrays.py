# Author: Kaustav Ghosh
# Problem: Count Strictly Increasing Subarrays
# Approach: Track the length of the strictly increasing run ending at each index; every such run of length L contributes L subarrays ending at that index, so add the run length as the scan goes and reset it to 1 whenever the sequence fails to increase

class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        run = 0
        for i, x in enumerate(nums):
            run = run + 1 if i and x > nums[i - 1] else 1
            total += run
        return total
