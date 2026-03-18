# Author: Kaustav Ghosh
# Problem: 1521 - Find a Value of a Mysterious Function Closest to Target
# Approach: Bitwise AND shrinks monotonically; sliding window with set of AND values

class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        result = float('inf')
        prev_set = set()

        for num in arr:
            curr_set = {num}
            for val in prev_set:
                curr_set.add(val & num)
            for val in curr_set:
                result = min(result, abs(val - target))
            prev_set = curr_set

        return result
