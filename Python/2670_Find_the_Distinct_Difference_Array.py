class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        return [
            len(set(nums[:i + 1])) - len(set(nums[i + 1:]))
            for i in range(n)
        ]
