# Author: Kaustav Ghosh
# Problem: Array With Elements Not Equal to Average of Neighbors
# Approach: An element fails only when it sits exactly between its neighbours, so making every interior element either strictly larger or strictly smaller than both of its neighbours removes the possibility entirely. Sorting and then swapping each adjacent pair starting from index one produces exactly that zigzag: after the swaps every odd position holds a value that was later in sorted order than both of its neighbours, and every interior even position holds one that was earlier than both. The numbers are distinct, so those comparisons are strict and no interior element can equal the average of two values that are both strictly above it or both strictly below it. Sorting dominates at O(n log n), and the swaps are done in place on a copy so the caller's list is untouched.

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ordered = sorted(nums)
        for index in range(1, len(ordered) - 1, 2):
            ordered[index], ordered[index + 1] = ordered[index + 1], ordered[index]
        return ordered
