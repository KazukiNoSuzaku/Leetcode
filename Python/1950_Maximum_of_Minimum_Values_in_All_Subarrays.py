# Author: Kaustav Ghosh
# Problem: Maximum of Minimum Values in All Subarrays
# Approach: For each element find the widest window in which it is the minimum, using previous/next strictly smaller boundaries. That element can be a window-minimum for that window size, so record it in that size bucket, then propagate maxima to smaller sizes (a min for a big window also serves smaller ones)

class Solution(object):
    def findMaximums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = [0] * (n + 1)
        for i in range(n):
            span = right[i] - left[i] - 1
            ans[span] = max(ans[span], nums[i])

        for size in range(n - 1, 0, -1):
            ans[size] = max(ans[size], ans[size + 1])

        return ans[1:]
