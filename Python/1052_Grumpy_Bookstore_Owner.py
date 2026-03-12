# Author: Kaustav Ghosh
# 1052. Grumpy Bookstore Owner
# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        base = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        # Sliding window: extra satisfied if we suppress grumpiness for 'minutes'
        extra = sum(customers[i] * grumpy[i] for i in range(minutes))
        max_extra = extra
        for i in range(minutes, n):
            extra += customers[i] * grumpy[i]
            extra -= customers[i - minutes] * grumpy[i - minutes]
            max_extra = max(max_extra, extra)
        return base + max_extra
