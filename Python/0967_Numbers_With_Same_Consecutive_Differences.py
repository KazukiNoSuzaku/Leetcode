# Return all non-negative integers of length n such that consecutive digits
# differ by exactly k. Answers may be in any order.

# Author: Kaustav Ghosh

class Solution(object):
    def numsSameConsecDiff(self, n, k):
        if n == 1: return list(range(10))
        res = []
        def dfs(num, length):
            if length == n:
                res.append(num)
                return
            last = num % 10
            if last + k <= 9:
                dfs(num * 10 + last + k, length + 1)
            if k != 0 and last - k >= 0:
                dfs(num * 10 + last - k, length + 1)
        for d in range(1, 10):
            dfs(d, 1)
        return res
