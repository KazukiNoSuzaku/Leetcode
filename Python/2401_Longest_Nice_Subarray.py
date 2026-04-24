class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        used = 0
        left = 0
        ans = 0
        for right, n in enumerate(nums):
            while used & n:
                used ^= nums[left]
                left += 1
            used |= n
            ans = max(ans, right - left + 1)
        return ans
