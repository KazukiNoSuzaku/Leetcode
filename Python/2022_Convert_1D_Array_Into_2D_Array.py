# Author: Kaustav Ghosh
# Problem 2022: Convert 1D Array Into 2D Array

class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m * n:
            return []
        return [original[i * n:(i + 1) * n] for i in range(m)]
