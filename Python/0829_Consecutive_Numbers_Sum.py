# Count ways to write n as sum of consecutive positive integers.

# Author: Kaustav Ghosh

class Solution(object):
    def consecutiveNumbersSum(self, n):
        count = 0
        k = 1
        while k * (k + 1) // 2 < n + 1:
            if (n - k * (k - 1) // 2) % k == 0:
                count += 1
            k += 1
        return count
