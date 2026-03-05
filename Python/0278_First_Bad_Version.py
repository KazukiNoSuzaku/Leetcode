# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example 1:
# Input: n = 5, bad = 4
# Output: 4

# Example 2:
# Input: n = 1, bad = 1
# Output: 1

# Constraints:
# 1 <= bad <= n <= 2^31 - 1

# Author: Kaustav Ghosh

def isBadVersion(version):
    pass  # provided by judge

class Solution(object):
    def firstBadVersion(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
