# Compute all n*(n+1)/2 subarray sums, sort them, return sum of indices left to right (1-indexed).

# Author: Kaustav Ghosh

class Solution(object):
    def rangeSum(self, nums, n, left, right):
        MOD = 10**9 + 7
        subs = []
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                subs.append(total)
        subs.sort()
        return sum(subs[left-1:right]) % MOD
