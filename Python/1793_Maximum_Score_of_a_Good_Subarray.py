# Author: Kaustav Ghosh
# Problem: Maximum Score of a Good Subarray
# Approach: The window must include index k. Expand outward from k, always stepping toward the taller neighbor so the minimum drops as slowly as possible, scoring min*width each step

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = right = k
        cur_min = nums[k]
        best = cur_min

        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] < nums[right + 1]:
                right += 1
            else:
                left -= 1
            cur_min = min(cur_min, nums[left], nums[right])
            best = max(best, cur_min * (right - left + 1))

        return best
