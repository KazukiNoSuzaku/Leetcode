# Author: Kaustav Ghosh
# Problem: Find All K-Distant Indices in an Array
# Approach: Every index within distance k of some position holding key is k-distant. Find the key positions, mark the covered ranges [j-k, j+k], and return the covered indices in order

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        covered = [False] * n
        for j in range(n):
            if nums[j] == key:
                lo = max(0, j - k)
                hi = min(n - 1, j + k)
                for i in range(lo, hi + 1):
                    covered[i] = True
        return [i for i in range(n) if covered[i]]
