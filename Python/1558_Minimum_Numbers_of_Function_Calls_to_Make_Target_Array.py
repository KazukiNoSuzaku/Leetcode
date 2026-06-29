# Author: Kaustav Ghosh
# Problem: Minimum Numbers of Function Calls to Make Target Array
# Approach: Work backwards; every set bit across all numbers is one increment, and the highest bit position sets how many shared doublings are needed

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        increments = 0
        max_doublings = 0
        for num in nums:
            increments += bin(num).count('1')
            if num > 0:
                max_doublings = max(max_doublings, num.bit_length() - 1)
        return increments + max_doublings
