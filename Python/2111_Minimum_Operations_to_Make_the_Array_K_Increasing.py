# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make the Array K-Increasing
# Approach: The k-increasing constraint couples only indices sharing the same remainder mod k, giving k independent subsequences that must each be non-decreasing. The fewest changes for one subsequence is its length minus its longest non-decreasing subsequence (patience sorting with bisect_right)

import bisect

class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        for r in range(k):
            sub = arr[r::k]
            tails = []
            for x in sub:
                idx = bisect.bisect_right(tails, x)
                if idx == len(tails):
                    tails.append(x)
                else:
                    tails[idx] = x
            total += len(sub) - len(tails)
        return total
