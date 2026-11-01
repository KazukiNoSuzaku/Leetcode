# Author: Kaustav Ghosh
# Problem: Check if Number is a Sum of Powers of Three
# Approach: Distinct powers of three summed together are exactly the numbers whose base-three representation uses only the digits zero and one, since a digit of two would mean reusing a power. Repeatedly dividing by three and inspecting the remainder reads those digits off from the least significant end, and a remainder of two immediately rules the number out.

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
