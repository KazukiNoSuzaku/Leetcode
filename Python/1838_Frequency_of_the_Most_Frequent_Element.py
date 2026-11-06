# Author: Kaustav Ghosh
# Problem: Frequency of the Most Frequent Element
# Approach: Whatever value ends up being the frequent one, the cheapest elements to raise to it are those already closest below it, which after sorting are contiguous, so the answer is the longest window that can be levelled up to its own largest member. Levelling a window costs its largest value times its length minus the sum it already holds, and that cost only grows as the window widens, so a sliding window that advances the left edge whenever the cost exceeds the budget visits each element twice. The running sum is maintained incrementally so each step is constant work.

class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        window = 0
        best = 1
        for right, value in enumerate(nums):
            window += value
            while value * (right - left + 1) - window > k:
                window -= nums[left]
                left += 1
            if right - left + 1 > best:
                best = right - left + 1
        return best
