# Author: Kaustav Ghosh
# Problem: Maximum Subarray Min-Product
# Approach: Every subarray has some element as its minimum, so instead of enumerating subarrays each element is considered as the minimum of the widest window it can dominate, which is bounded by the nearest strictly smaller value on either side; any narrower window with the same minimum has a smaller sum and so is never better. Those boundaries come out of one monotonic stack pass: an element is popped exactly when a value at least as small arrives, which fixes its right edge, and whatever is left beneath it fixes its left edge. A prefix-sum array turns the window's sum into one subtraction, and a sentinel at the end flushes the stack. The modulus is applied only to the final answer so the comparisons stay exact.

class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for index, value in enumerate(nums):
            prefix[index + 1] = prefix[index] + value

        best = 0
        stack = []
        for index in range(n + 1):
            current = nums[index] if index < n else 0
            while stack and nums[stack[-1]] >= current:
                top = stack.pop()
                left = stack[-1] + 1 if stack else 0
                product = nums[top] * (prefix[index] - prefix[left])
                if product > best:
                    best = product
            stack.append(index)
        return best % MOD
