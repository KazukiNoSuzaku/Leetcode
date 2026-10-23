# Author: Kaustav Ghosh
# Problem: Find the Most Competitive Subsequence
# Approach: Smaller earlier is always better, so whenever the value just chosen is larger than the one now being considered, dropping it improves the result, provided enough elements remain to still fill the required length. That makes this a monotonic stack: each element pops any larger predecessors that can afford to be discarded and is then pushed itself. Every element is pushed and popped at most once, so the whole thing is linear, and the stack is truncated to k at the end because the tail may legitimately be longer than needed.

class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        chosen = []
        for i, value in enumerate(nums):
            # Pop only while the remaining elements can still fill k slots.
            while chosen and chosen[-1] > value and len(chosen) + (n - i) > k:
                chosen.pop()
            if len(chosen) < k:
                chosen.append(value)
        return chosen
