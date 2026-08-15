# Author: Kaustav Ghosh
# Problem: Convert 1D Array Into 2D Array
# Approach: The reshape is possible only when the element count equals m*n. Slice the flat array into m consecutive rows of length n

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
