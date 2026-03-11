# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix
# into a new one with a different size r x c keeping its original data.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix.

# Author: Kaustav Ghosh

class Solution(object):
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        if m * n != r * c: return mat
        flat = [mat[i][j] for i in range(m) for j in range(n)]
        return [flat[i*c:(i+1)*c] for i in range(r)]
