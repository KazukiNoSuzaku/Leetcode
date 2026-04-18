# Author: Kaustav Ghosh
# 2340. Minimum Adjacent Swaps to Make a Valid Array
# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/
# Premium: find leftmost 0 and rightmost 1, count swaps; adjust if they cross

class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Find leftmost 0
        left = -1
        for i in range(n):
            if nums[i] == 0:
                left = i
                break

        # Find rightmost 1
        right = -1
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                right = i
                break

        # If no 0 or no 1 exists, already valid
        if left == -1 or right == -1:
            return 0

        # Swaps to move leftmost 0 to front: left steps
        # Swaps to move rightmost 1 to back: (n - 1 - right) steps
        # If left >= right, they point to same element or cross: one less swap needed
        swaps = left + (n - 1 - right)
        if left >= right:
            swaps -= 1

        return swaps
