# Author: Kaustav Ghosh
# Problem: Closest Fair Integer
# Approach: A number with an odd count of digits can never be fair, so whenever the candidate has odd length jump straight to the smallest number one digit longer. Within an even length, fair numbers are dense enough that stepping up one at a time and counting odd digits reaches the answer quickly

class Solution(object):
    def closestFair(self, n):
        """
        :type n: int
        :rtype: int
        """
        while True:
            digits = str(n)
            if len(digits) % 2:
                n = 10 ** len(digits)
                continue
            if sum(int(d) % 2 for d in digits) * 2 == len(digits):
                return n
            n += 1
