# Author: Kaustav Ghosh
# Problem: Sum of Digits in Base K
# Approach: The digits of a number in base k are the successive remainders when it is repeatedly divided by k, read from the least significant end. Since only their sum is wanted the digits never have to be stored or reversed, so one loop accumulating the remainders is enough.

class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        total = 0
        while n:
            n, digit = divmod(n, k)
            total += digit
        return total
