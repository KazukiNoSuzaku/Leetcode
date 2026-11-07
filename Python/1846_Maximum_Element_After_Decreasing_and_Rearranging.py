# Author: Kaustav Ghosh
# Problem: Maximum Element After Decreasing and Rearranging
# Approach: Values may only be lowered and the final array has to start at one and climb by at most one each step, so the best arrangement is the sorted one: putting a larger value earlier would waste it, since position i can never hold more than i + 1 anyway. Walking the sorted values and capping each at one above its predecessor therefore produces the tallest legal array, and the last cap is the answer.

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        highest = 0
        for value in sorted(arr):
            if value > highest:
                highest += 1
        return highest
