# Author: Kaustav Ghosh
# Problem: Generate a String With Characters That Have Odd Counts
# Approach: n 'a's if n is odd; (n-1) 'a's + 1 'b' if n is even

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2 == 1:
            return 'a' * n
        return 'a' * (n - 1) + 'b'
