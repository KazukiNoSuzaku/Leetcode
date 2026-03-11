# Find minimum score after adding +k or -k to each element.

# Author: Kaustav Ghosh

class Solution(object):
    def smallestRangeII(self, nums, k):
        nums.sort()
        n = len(nums)
        res = nums[-1] - nums[0]
        for i in range(n - 1):
            high = max(nums[-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i+1] - k)
            res = min(res, high - low)
        return res
