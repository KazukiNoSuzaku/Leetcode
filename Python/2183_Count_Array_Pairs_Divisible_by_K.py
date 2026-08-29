# Author: Kaustav Ghosh
# Problem: Count Array Pairs Divisible by K
# Approach: A product nums[i]*nums[j] is divisible by k exactly when gcd(nums[i],k)*gcd(nums[j],k) is divisible by k. Bucket each element by g = gcd(value, k) (always a divisor of k), then count pairs of buckets whose gcd values multiply to a multiple of k

from math import gcd
from collections import defaultdict


class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        buckets = defaultdict(int)
        for x in nums:
            buckets[gcd(x, k)] += 1

        keys = list(buckets.keys())
        total = 0
        for i in range(len(keys)):
            for j in range(i, len(keys)):
                d1, d2 = keys[i], keys[j]
                if (d1 * d2) % k == 0:
                    if i == j:
                        c = buckets[d1]
                        total += c * (c - 1) // 2
                    else:
                        total += buckets[d1] * buckets[d2]
        return total
