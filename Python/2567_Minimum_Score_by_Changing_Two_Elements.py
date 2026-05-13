class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        # Change 2 elements: compare removing 2 largest, 2 smallest, or one of each.
        if len(nums) <= 2:
            return 0
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])
