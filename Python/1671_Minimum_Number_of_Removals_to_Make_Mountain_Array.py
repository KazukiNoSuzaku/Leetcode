# Author: Kaustav Ghosh
# Problem: Minimum Number of Removals to Make Mountain Array
# Approach: For every possible peak compute the longest increasing run ending there and decreasing run starting there; the best valid mountain minimizes removals n - (LIS + LDS - 1)

class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)

        lds = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)

        best = 0
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:  # peak needs both sides
                best = max(best, lis[i] + lds[i] - 1)
        return n - best
