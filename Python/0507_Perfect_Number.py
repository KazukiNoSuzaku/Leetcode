# A perfect number is a positive integer that is equal to the sum of its positive divisors,
# excluding the number itself. Return true if num is a perfect number.

# Author: Kaustav Ghosh

class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1: return False
        total = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
            i += 1
        return total == num
