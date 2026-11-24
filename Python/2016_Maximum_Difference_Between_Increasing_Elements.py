# Author: Kaustav Ghosh
# Problem: Maximum Difference Between Increasing Elements
# Approach: For a fixed later element the best possible difference comes from pairing it with the smallest element anywhere before it, so carrying the running minimum while sweeping left to right gives every element's best partner for free. Each element is compared against that running minimum and the largest strictly positive difference found is the answer, with the minimum updated afterwards so an element is never paired with itself. If no element ever exceeds something before it, no valid pair exists and the result stays at minus one.

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = nums[0]
        best = -1
        for value in nums[1:]:
            if value > smallest and value - smallest > best:
                best = value - smallest
            elif value < smallest:
                smallest = value
        return best
