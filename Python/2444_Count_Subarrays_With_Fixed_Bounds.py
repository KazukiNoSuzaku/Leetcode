# Author: Kaustav Ghosh
# Problem: Count Subarrays With Fixed Bounds
# Approach: A valid subarray contains no value outside [minK, maxK] and holds at least one of each bound. Scanning once and remembering the last index of a forbidden value, of minK and of maxK, every start after the forbidden index and at or before both bound positions works, which is min(last minK, last maxK) - last forbidden subarrays ending here

class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        total = 0
        last_bad = last_min = last_max = -1
        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                last_bad = i
            if x == minK:
                last_min = i
            if x == maxK:
                last_max = i
            total += max(0, min(last_min, last_max) - last_bad)
        return total
