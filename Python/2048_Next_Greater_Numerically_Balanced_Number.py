# Author: Kaustav Ghosh
# Problem: Next Greater Numerically Balanced Number
# Approach: A balanced number's digit counts must each equal the digit itself, which means the digits present partition the number's length into distinct parts, so balanced numbers are sparse but still close enough together to walk between: across the whole allowed input range the widest gap runs from 666666 up to 1224444, so no search covers more than about half a million candidates. That makes walking upward from the next integer and testing each one practical, and the test is cheap because peeling digits off with division fills a ten-slot tally that is then checked against the digits it recorded. A zero digit can never satisfy the rule, since being present means appearing at least once, so any number containing a zero is rejected by the same check without a special case.

class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def balanced(value):
            counts = [0] * 10
            while value:
                counts[value % 10] += 1
                value //= 10
            for digit in range(10):
                if counts[digit] and counts[digit] != digit:
                    return False
            return True

        candidate = n + 1
        while not balanced(candidate):
            candidate += 1
        return candidate
