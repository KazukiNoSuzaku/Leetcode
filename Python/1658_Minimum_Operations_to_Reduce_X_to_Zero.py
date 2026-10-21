# Author: Kaustav Ghosh
# Problem: Minimum Operations to Reduce X to Zero
# Approach: The removed elements always form a prefix and a suffix, so what remains is a contiguous middle block, and removing the fewest elements is the same as keeping the longest such block; since the removed total must be exactly x, the kept block must sum to the array total minus x. All values are positive, which makes the running sum strictly increasing and lets a sliding window find the longest block of a given sum in one pass: the window grows on the right and is shrunk from the left while its sum is too large. A required total below zero, or no window ever reaching it, means it cannot be done.

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        wanted = sum(nums) - x
        if wanted < 0:
            return -1
        if wanted == 0:
            return len(nums)

        longest = -1
        running = 0
        left = 0
        for right, value in enumerate(nums):
            running += value
            while running > wanted:
                running -= nums[left]
                left += 1
            if running == wanted and right - left + 1 > longest:
                longest = right - left + 1
        return -1 if longest < 0 else len(nums) - longest
