# Author: Kaustav Ghosh
# Problem: 1558 - Minimum Numbers of Function Calls to Make Target Array
# Approach: Count set bits (add 1 ops) + max bit length (double ops)

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        add_ops = sum(bin(n).count('1') for n in nums)
        double_ops = max(n.bit_length() - 1 if n > 0 else 0 for n in nums)
        return add_ops + double_ops
