# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Count frequency of each position in sideLength tile, pick top maxOnes

class Solution(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        """
        :type width: int
        :type height: int
        :type sideLength: int
        :type maxOnes: int
        :rtype: int
        """
        counts = []
        for i in range(sideLength):
            for j in range(sideLength):
                # Count how many sideLength x sideLength submatrices include position (i,j)
                rows = (height - 1 - i) // sideLength + 1
                cols = (width - 1 - j) // sideLength + 1
                counts.append(rows * cols)
        counts.sort(reverse=True)
        return sum(counts[:maxOnes])
