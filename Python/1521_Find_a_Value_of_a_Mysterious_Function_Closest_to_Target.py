# Author: Kaustav Ghosh
# Problem: Find a Value of a Mysterious Function Closest to Target
# Approach: Maintain set of distinct AND values ending at each index (at most 32); check each against target

class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        ans = float('inf')
        prev = set()
        for num in arr:
            curr = {num}
            for v in prev:
                curr.add(v & num)
            for v in curr:
                ans = min(ans, abs(v - target))
            prev = curr
        return ans
