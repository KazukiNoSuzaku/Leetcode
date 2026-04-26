class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Max AND of any subarray = max element (AND only clears bits)
        # Longest subarray achieving max AND = longest consecutive run of max elements
        m = max(nums)
        ans = run = 0
        for x in nums:
            if x == m:
                run += 1
                ans = max(ans, run)
            else:
                run = 0
        return ans
