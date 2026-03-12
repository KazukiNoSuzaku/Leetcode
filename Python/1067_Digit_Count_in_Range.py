# Author: Kaustav Ghosh
# 1067. Digit Count in Range
# https://leetcode.com/problems/digit-count-in-range/

class Solution(object):
    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        def count_digit(n, d):
            if n < 0:
                return 0
            result = 0
            factor = 1
            while factor <= n:
                higher = n // (factor * 10)
                current = (n // factor) % 10
                lower = n % factor
                if d == 0:
                    result += (higher - 1) * factor + min(lower + 1, factor)
                elif current < d:
                    result += higher * factor
                elif current == d:
                    result += higher * factor + lower + 1
                else:
                    result += (higher + 1) * factor
                factor *= 10
            return result

        return count_digit(high, d) - count_digit(low - 1, d)
