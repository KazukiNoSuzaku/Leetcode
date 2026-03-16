# Author: Kaustav Ghosh
# Problem: Sort Integers by The Power Value
# Approach: Cache Collatz steps, sort by power value

class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        cache = {1: 0}

        def power(n):
            if n in cache:
                return cache[n]
            if n % 2 == 0:
                cache[n] = 1 + power(n // 2)
            else:
                cache[n] = 1 + power(3 * n + 1)
            return cache[n]

        nums = list(range(lo, hi + 1))
        nums.sort(key=lambda x: (power(x), x))
        return nums[k - 1]
