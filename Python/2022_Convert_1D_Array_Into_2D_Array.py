# Author: Kaustav Ghosh
# Problem: Convert 1D Array Into 2D Array
# Approach: The reshape is possible exactly when the requested rows times columns equals the number of elements available, since every element must be used and none may be invented, so that single product check decides the impossible case outright. When it holds, the original order is preserved row by row, meaning row number r is simply the slice of the original starting at r times the column count and running for that many entries. Slicing each row directly avoids tracking an index by hand and copies each element once.

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
        return [original[row * n:(row + 1) * n] for row in range(m)]
