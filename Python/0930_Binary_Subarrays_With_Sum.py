# Count subarrays with binary sum equal to goal.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = defaultdict(int)
        count[0] = 1
        prefix = res = 0
        for x in nums:
            prefix += x
            res += count[prefix - goal]
            count[prefix] += 1
        return res
