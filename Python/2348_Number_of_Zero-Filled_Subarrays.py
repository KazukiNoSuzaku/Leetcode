# Author: Kaustav Ghosh
# Problem: Number of Zero-Filled Subarrays
# Approach: Track the length of the current run of zeros; each zero ends exactly run-length zero-filled subarrays, so add the run length at every zero and reset it at any non-zero

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = run = 0
        for x in nums:
            if x == 0:
                run += 1
                total += run
            else:
                run = 0
        return total
