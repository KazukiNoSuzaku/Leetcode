# Author: Kaustav Ghosh
# Problem: Sum of Digits in Base K
# Approach: Repeatedly take n mod k to peel off base-k digits and add them (the sum stays a base-10 number)

class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        total = 0
        while n:
            total += n % k
            n //= k
        return total
