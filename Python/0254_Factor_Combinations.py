# Numbers can be regarded as the product of their factors.
# Given an integer n, return all possible combinations of its factors.
# Note that the factors should be in the range [2, n - 1].

# Example 1:
# Input: n = 1
# Output: []

# Example 2:
# Input: n = 12
# Output: [[2,6],[3,4],[2,2,3]]

# Constraints:
# 1 <= n <= 10^7

# Author: Kaustav Ghosh

class Solution(object):
    def getFactors(self, n):
        res = []
        def dfs(n, start, path):
            if path:
                res.append(path + [n])
            i = start
            while i * i <= n:
                if n % i == 0:
                    dfs(n // i, i, path + [i])
                i += 1
        dfs(n, 2, [])
        return res
