# Author: Kaustav Ghosh
# Problem: Find a Value of a Mysterious Function Closest to Target
# Approach: The function is the bitwise AND over a subarray, and extending a subarray can only clear bits, so the distinct ANDs of all subarrays ending at one index number only about as many as there are bits. Carry that small set forward, AND-ing it with each new element, and measure every value against the target

class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        best = abs(arr[0] - target)
        ending_here = set()
        for x in arr:
            ending_here = {x} | {value & x for value in ending_here}
            for value in ending_here:
                best = min(best, abs(value - target))
        return best
