# Author: Kaustav Ghosh

class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        xor = [[0] * (n + 1) for _ in range(m + 1)]
        vals = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                xor[i][j] = xor[i-1][j] ^ xor[i][j-1] ^ xor[i-1][j-1] ^ matrix[i-1][j-1]
                vals.append(xor[i][j])
        vals.sort(reverse=True)
        return vals[k - 1]
