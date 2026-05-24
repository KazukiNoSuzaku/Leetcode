class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        nums = [sorted(row, reverse=True) for row in nums]
        return sum(
            max(nums[r][c] for r in range(len(nums)))
            for c in range(len(nums[0]))
        )
