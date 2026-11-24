# Author: Kaustav Ghosh
# Problem: Sum of Beauty in the Array
# Approach: The two-point test asks whether an element beats everything before it and is beaten by everything after it, which only needs the largest value to its left and the smallest value to its right rather than any repeated scanning. Those are precomputed as a prefix maximum and a suffix minimum, after which each interior index is classified in constant time: two points when it clears both extremes, otherwise one point when it merely sits strictly between its immediate neighbours, and nothing when neither holds. Three linear passes in total.

class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        largest_before = [0] * total
        running = nums[0]
        for index in range(1, total):
            largest_before[index] = running
            if nums[index] > running:
                running = nums[index]

        smallest_after = [0] * total
        running = nums[total - 1]
        for index in range(total - 2, -1, -1):
            smallest_after[index] = running
            if nums[index] < running:
                running = nums[index]

        beauty = 0
        for index in range(1, total - 1):
            if nums[index] > largest_before[index] and nums[index] < smallest_after[index]:
                beauty += 2
            elif nums[index - 1] < nums[index] < nums[index + 1]:
                beauty += 1
        return beauty
