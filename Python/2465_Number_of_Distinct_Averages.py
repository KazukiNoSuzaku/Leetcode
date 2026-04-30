class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        seen = set()
        l, r = 0, len(nums) - 1
        while l < r:
            seen.add(nums[l] + nums[r])  # same denominator, so distinct sums = distinct averages
            l += 1
            r -= 1
        return len(seen)
