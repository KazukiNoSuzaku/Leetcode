class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        # Running left sum; right sum = total - leftSum - nums[i]; answer is absolute difference.
        total = sum(nums)
        left = 0
        result = []
        for x in nums:
            result.append(abs(left - (total - left - x)))
            left += x
        return result
