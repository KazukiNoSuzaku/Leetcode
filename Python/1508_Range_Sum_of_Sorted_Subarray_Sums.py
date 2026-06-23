# Author: Kaustav Ghosh
# Problem: Range Sum of Sorted Subarray Sums
# Approach: Generate all subarray sums, sort, sum the slice [left-1, right]

class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        sums = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                sums.append(s)
        sums.sort()
        return sum(sums[left - 1:right]) % MOD
