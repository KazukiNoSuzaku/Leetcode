# Premium problem
# dp[i] = number of strictly increasing subarrays ending at index i
# If nums[i] > nums[i-1]: dp[i] = dp[i-1] + 1, else dp[i] = 1
# Answer = sum of all dp[i]

class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        ans = run = 1
        for i in range(1, len(nums)):
            run = run + 1 if nums[i] > nums[i - 1] else 1
            ans += run
        return ans
