from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        # Sort; for each i binary-search the valid range of j > i in the remaining suffix.
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            lo = bisect_left(nums, lower - nums[i], i + 1, n)
            hi = bisect_right(nums, upper - nums[i], i + 1, n)
            ans += hi - lo
        return ans
