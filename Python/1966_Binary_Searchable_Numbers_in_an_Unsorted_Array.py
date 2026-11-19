# Author: Kaustav Ghosh
# Problem: Binary Searchable Numbers in an Unsorted Array
# Approach: The search only ever discards a side of the current window, so a target is guaranteed to be found exactly when no pivot choice can ever throw it away. A pivot to the left of the target discards everything left of itself, which is safe, unless that pivot is larger than the target, in which case it discards the target's side; likewise a pivot to the right is safe unless it is smaller than the target. So a value survives every possible pivot sequence precisely when it is greater than everything before it and smaller than everything after it. One forward pass marks the positions that beat their running prefix maximum and one backward pass marks those below their running suffix minimum, and the count of positions marked by both is the answer, in O(n) time.

class Solution(object):
    def binarySearchableNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        safe = [True] * total

        tallest = None
        for index in range(total):
            if tallest is not None and nums[index] < tallest:
                safe[index] = False
            elif tallest is None or nums[index] > tallest:
                tallest = nums[index]

        smallest = None
        for index in range(total - 1, -1, -1):
            if smallest is not None and nums[index] > smallest:
                safe[index] = False
            elif smallest is None or nums[index] < smallest:
                smallest = nums[index]

        return sum(1 for flag in safe if flag)
