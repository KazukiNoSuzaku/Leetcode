# Author: Kaustav Ghosh
# Problem: Find the Most Competitive Subsequence
# Approach: Monotonic stack; pop larger trailing elements while enough remain to still reach length k, keeping the stack smallest-lexicographic

class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        stack = []
        for i, x in enumerate(nums):
            # Can drop stack[-1] only if remaining elements can still fill k
            while stack and stack[-1] > x and len(stack) - 1 + (n - i) >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(x)
        return stack
