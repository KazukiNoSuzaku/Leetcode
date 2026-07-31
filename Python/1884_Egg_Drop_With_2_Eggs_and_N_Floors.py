# Author: Kaustav Ghosh
# Problem: Egg Drop With 2 Eggs and N Floors
# Approach: With t drops the first egg can start at floor t and step down by one each break, covering t + (t-1) + ... + 1 floors; the answer is the smallest t whose triangular number reaches n

class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = 1
        while t * (t + 1) // 2 < n:
            t += 1
        return t
