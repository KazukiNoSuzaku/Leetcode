# Author: Kaustav Ghosh
# Problem: Minimize Maximum Pair Sum in Array
# Approach: Pairing the smallest remaining value with the largest keeps the big values from meeting each other, which is what drives the maximum up: if two pairs were arranged otherwise, swapping their partners so that the larger value takes the smaller partner never raises the worse of the two sums. So sorting and pairing across from both ends is optimal, and the answer is the largest of those n over two sums.

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ordered = sorted(nums)
        return max(ordered[i] + ordered[-1 - i] for i in range(len(ordered) // 2))
