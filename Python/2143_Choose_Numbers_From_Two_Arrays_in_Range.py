# Author: Kaustav Ghosh
# Problem: Choose Numbers From Two Arrays in Range
# Approach: A range is balanced when, choosing +nums1[i] or -nums2[i] at each index, the signed total is zero (sum picked from nums1 equals sum picked from nums2). For each start index, extend the range while maintaining a count of achievable signed sums; add the count of zero-sums after each extension

from collections import defaultdict

class Solution(object):
    def countSubranges(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums1)
        total = 0
        for l in range(n):
            ways = defaultdict(int)
            ways[0] = 1
            for r in range(l, n):
                a, b = nums1[r], nums2[r]
                new = defaultdict(int)
                for s, c in ways.items():
                    new[s + a] = (new[s + a] + c) % MOD
                    new[s - b] = (new[s - b] + c) % MOD
                ways = new
                total = (total + ways[0]) % MOD
        return total
