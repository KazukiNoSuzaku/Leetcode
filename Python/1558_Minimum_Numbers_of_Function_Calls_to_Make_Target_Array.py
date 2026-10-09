# Author: Kaustav Ghosh
# Problem: Minimum Numbers of Function Calls to Make Target Array
# Approach: Run the process backwards: every set bit in a number must have been placed by its own increment, so the increments total the set bits across the array. Doubling applies to the whole array at once, so it is needed as many times as the longest number has bits beyond the first

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        increments = 0
        widest = 0
        for x in nums:
            increments += bin(x).count('1')
            widest = max(widest, x.bit_length())
        return increments + max(0, widest - 1)
