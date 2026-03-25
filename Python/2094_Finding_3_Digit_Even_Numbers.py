# Author: Kaustav Ghosh
# Problem 2094: Finding 3-Digit Even Numbers

from collections import Counter

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        count = Counter(digits)
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            needed = Counter([d1, d2, d3])
            valid = True
            for d, c in needed.items():
                if count[d] < c:
                    valid = False
                    break
            if valid:
                result.append(num)
        return result
