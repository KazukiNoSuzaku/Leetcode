# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Two pointers on customfunction

class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type customfunction: CustomFunction
        :type z: int
        :rtype: List[List[int]]
        """
        result = []
        x, y = 1, 1000
        while x <= 1000 and y >= 1:
            val = customfunction.f(x, y)
            if val == z:
                result.append([x, y])
                x += 1
                y -= 1
            elif val < z:
                x += 1
            else:
                y -= 1
        return result
