# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# - Only numbers 1 through 9 are used.
# - Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice,
# and the combinations may be returned in any order.

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]

# Constraints:
# 2 <= k <= 9
# 1 <= n <= 60

# Author: Kaustav Ghosh

class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        def backtrack(start, path, remaining):
            if len(path) == k and remaining == 0:
                res.append(list(path))
                return
            if len(path) == k or remaining <= 0:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, remaining - i)
                path.pop()
        backtrack(1, [], n)
        return res
