# Check if array can be split into two groups with same average.

# Author: Kaustav Ghosh

class Solution(object):
    def splitArraySameAverage(self, nums):
        n = len(nums)
        total = sum(nums)
        half = n // 2
        possible = [set() for _ in range(half + 1)]
        possible[0].add(0)
        for num in nums:
            for k in range(min(half, half), 0, -1):
                for s in possible[k-1]:
                    possible[k].add(s + num)
        for k in range(1, half + 1):
            if total * k % n == 0 and total * k // n in possible[k]:
                return True
        return False
