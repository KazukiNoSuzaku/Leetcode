# Given an integer n, return all the strobogrammatic numbers that are of length n.
# You may return the answer in any order.
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Example 1:
# Input: n = 2
# Output: ["11","69","88","96"]

# Example 2:
# Input: n = 1
# Output: ["0","1","8"]

# Constraints:
# 1 <= n <= 14

# Author: Kaustav Ghosh

class Solution(object):
    def findStrobogrammatic(self, n):
        def helper(n, total):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']
            middles = helper(n - 2, total)
            res = []
            for mid in middles:
                for a, b in [('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')]:
                    if n != total or a != '0':
                        res.append(a + mid + b)
            return res
        return helper(n, n)
