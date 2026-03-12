# Author: Kaustav Ghosh
# Greedy: assign 2s to both rows, then distribute remaining 1s

class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = len(colsum)
        top = [0] * n
        bot = [0] * n

        for j in range(n):
            if colsum[j] == 2:
                top[j] = 1
                bot[j] = 1
                upper -= 1
                lower -= 1

        for j in range(n):
            if colsum[j] == 1:
                if upper > lower:
                    top[j] = 1
                    upper -= 1
                else:
                    bot[j] = 1
                    lower -= 1

        if upper != 0 or lower != 0:
            return []
        return [top, bot]
