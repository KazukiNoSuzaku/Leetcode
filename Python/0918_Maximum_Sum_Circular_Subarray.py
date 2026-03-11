# Find maximum sum subarray in a circular array.

# Author: Kaustav Ghosh

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)
        max_sum = cur_max = nums[0]
        min_sum = cur_min = nums[0]
        for x in nums[1:]:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)
