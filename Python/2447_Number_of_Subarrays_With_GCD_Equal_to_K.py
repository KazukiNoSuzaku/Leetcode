# Author: Kaustav Ghosh
# Problem: Number of Subarrays With GCD Equal to K
# Approach: Keep the distinct gcds of all subarrays ending at the current index with how many subarrays give each one. Extending by one element maps every gcd g to gcd(g, x), and since each step at least halves any value that changes, only a logarithmic number of distinct gcds survive. An element not divisible by k clears the set, because k must divide every member of the subarray

from math import gcd


class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        ending_here = {}
        for x in nums:
            nxt = {}
            if x % k == 0:
                nxt[x] = 1
                for g, count in ending_here.items():
                    merged = gcd(g, x)
                    nxt[merged] = nxt.get(merged, 0) + count
            ending_here = nxt
            total += ending_here.get(k, 0)
        return total
