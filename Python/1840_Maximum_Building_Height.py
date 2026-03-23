# Author: Kaustav Ghosh
# Problem 1840: Maximum Building Height

class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        m = len(restrictions)
        # Forward pass: limit height based on previous restriction
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0])
        # Backward pass: limit height based on next restriction
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0])
        # Find max height between consecutive restrictions
        result = 0
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            h = (dist + restrictions[i][1] + restrictions[i - 1][1]) // 2
            result = max(result, h)
        return result
