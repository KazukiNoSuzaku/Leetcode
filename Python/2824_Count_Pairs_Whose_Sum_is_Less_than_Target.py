class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans, left, right = 0, 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                ans += right - left
                left += 1
            else:
                right -= 1
        return ans
