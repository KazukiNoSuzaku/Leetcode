# Partition array into two intervals where all left <= all right.

# Author: Kaustav Ghosh

class Solution(object):
    def partitionDisjoint(self, nums):
        n = len(nums)
        max_left = [0] * n
        min_right = [0] * n
        max_left[0] = nums[0]
        for i in range(1, n): max_left[i] = max(max_left[i-1], nums[i])
        min_right[-1] = nums[-1]
        for i in range(n-2, -1, -1): min_right[i] = min(min_right[i+1], nums[i])
        for i in range(n-1):
            if max_left[i] <= min_right[i+1]: return i + 1
        return n
