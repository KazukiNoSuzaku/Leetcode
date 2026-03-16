# Author: Kaustav Ghosh
# Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Approach: Two monotone deques tracking min and max in sliding window

from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_dq = deque()
        min_dq = deque()
        left = 0
        result = 0
        for right in range(len(nums)):
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            max_dq.append(right)
            min_dq.append(right)
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()
            result = max(result, right - left + 1)
        return result
