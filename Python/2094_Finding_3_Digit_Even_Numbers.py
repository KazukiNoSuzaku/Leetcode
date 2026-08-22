# Author: Kaustav Ghosh
# Problem: Finding 3-Digit Even Numbers
# Approach: For every even three-digit number, check whether its digits can be drawn from the available multiset of digits; collect those that can

from collections import Counter

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        available = Counter(digits)
        result = []
        for num in range(100, 1000, 2):
            need = Counter(int(c) for c in str(num))
            if all(available[d] >= cnt for d, cnt in need.items()):
                result.append(num)
        return result
