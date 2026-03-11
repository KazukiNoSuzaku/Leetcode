# Given an integer array nums, consider every node i, j where nums[i] and nums[j]
# share a common factor > 1. Return the size of the largest connected component.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def largestComponentSize(self, nums):
        parent = list(range(max(nums) + 1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            parent[find(x)] = find(y)
        for n in nums:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    union(n, i)
                    union(n, n // i)
                i += 1
        count = Counter(find(n) for n in nums)
        return max(count.values())
