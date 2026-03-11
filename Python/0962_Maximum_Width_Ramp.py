# A ramp is a pair (i, j) where i < j and nums[i] <= nums[j].
# Return the maximum width j - i of such a ramp.

# Author: Kaustav Ghosh

class Solution(object):
    def maxWidthRamp(self, nums):
        n = len(nums)
        # Build decreasing stack from left
        stack = []
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        res = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                res = max(res, j - stack.pop())
        return res
