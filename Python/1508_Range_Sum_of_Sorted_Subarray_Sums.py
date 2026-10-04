# Author: Kaustav Ghosh
# Problem: Range Sum of Sorted Subarray Sums
# Approach: There are only n * (n + 1) / 2 subarrays, which the limits keep small enough to list outright: accumulate each start's running totals, sort them all, then add up the requested one-indexed slice modulo 1e9 + 7

class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        sums = []
        for i in range(n):
            running = 0
            for j in range(i, n):
                running += nums[j]
                sums.append(running)
        sums.sort()
        return sum(sums[left - 1:right]) % (10 ** 9 + 7)
