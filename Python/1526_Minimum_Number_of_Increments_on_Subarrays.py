# Author: Kaustav Ghosh
# Problem: Minimum Number of Increments on Subarrays (Premium)
# Approach: Each rise from target[i-1] to target[i] requires that many additional operations; sum all positive diffs plus target[0]

class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        ans = target[0]
        for i in range(1, len(target)):
            ans += max(0, target[i] - target[i - 1])
        return ans
