# Find the length of the smallest positive integer consisting only of 1s
# that is divisible by k. Return -1 if none exists.

# Author: Kaustav Ghosh

class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1
        rem = 0
        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length
        return -1
