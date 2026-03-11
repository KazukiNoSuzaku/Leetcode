# Find the number that appears twice and the number that is missing in array [1..n].

# Author: Kaustav Ghosh

class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        dup = miss = -1
        for i in range(1, n + 1):
            if count.get(i, 0) == 2: dup = i
            if count.get(i, 0) == 0: miss = i
        return [dup, miss]
