# Author: Kaustav Ghosh
# Problem 2048: Next Greater Numerically Balanced Number

class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_balanced(num):
            s = str(num)
            for c in s:
                if s.count(c) != int(c):
                    return False
            return True

        candidate = n + 1
        while not is_balanced(candidate):
            candidate += 1
        return candidate
