# Author: Kaustav Ghosh
# Problem: Check if Number is a Sum of Powers of Three
# Approach: Each power of three may be used at most once, so n works iff its base-3 representation has no digit equal to 2

class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True
