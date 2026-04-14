# Author: Kaustav Ghosh
class Solution(object):
    def countSubarrays(self, nums, k):
        # type: (List[int], int) -> int
        res = 0
        left = 0
        s = 0
        for right in range(len(nums)):
            s += nums[right]
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            res += right - left + 1
        return res
