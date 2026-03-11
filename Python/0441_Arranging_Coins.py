# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# Return the number of complete rows of the staircase you will be able to form.

# Author: Kaustav Ghosh

class Solution(object):
    def arrangeCoins(self, n):
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
