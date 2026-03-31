# Author: Kaustav Ghosh
# 2183. Count Array Pairs Divisible by K
# https://leetcode.com/problems/count-array-pairs-divisible-by-k/
# Difficulty: Hard
#
# Approach: For each number, compute g = gcd(nums[i], k). We need
# gcd(nums[i], k) * gcd(nums[j], k) to be divisible by k.
# Group numbers by their gcd with k, then for each pair of groups (a, b)
# where a*b % k == 0, count the pairs.
# Time: O(n * d(k)), Space: O(d(k)) where d(k) is number of divisors of k

from math import gcd
from collections import defaultdict

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        for num in nums:
            freq[gcd(num, k)] += 1

        divisors = list(freq.keys())
        count = 0

        for i in range(len(divisors)):
            for j in range(i, len(divisors)):
                a, b = divisors[i], divisors[j]
                if (a * b) % k == 0:
                    if i == j:
                        count += freq[a] * (freq[a] - 1) // 2
                    else:
                        count += freq[a] * freq[b]

        return count
