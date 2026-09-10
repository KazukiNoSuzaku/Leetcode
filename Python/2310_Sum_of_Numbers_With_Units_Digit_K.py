# Author: Kaustav Ghosh
# Problem: Sum of Numbers With Units Digit K
# Approach: If the set has c numbers each ending in digit k, their sum ends in the last digit of c*k, which must match num's last digit, and c*k cannot exceed num (the minimum possible sum with c such numbers). Try counts 1..10 (units digits cycle) and return the smallest valid c; 0 if num is already 0, else -1

class Solution(object):
    def minimumNumbers(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        if num == 0:
            return 0
        for c in range(1, 11):
            if c * k <= num and (c * k) % 10 == num % 10:
                return c
        return -1
