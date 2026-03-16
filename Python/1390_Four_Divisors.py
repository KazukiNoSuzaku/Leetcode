# Author: Kaustav Ghosh
# Problem: Four Divisors
# Approach: For each number find exactly 4 divisors, sum them

import math

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for n in nums:
            divisors = []
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)
                    if len(divisors) > 4:
                        break
            if len(divisors) == 4:
                result += sum(divisors)
        return result
