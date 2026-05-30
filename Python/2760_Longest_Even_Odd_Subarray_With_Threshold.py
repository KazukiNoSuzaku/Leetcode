class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        i = 0
        while i < n:
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                j = i + 1
                while j < n and nums[j] <= threshold and nums[j] % 2 != nums[j - 1] % 2:
                    j += 1
                ans = max(ans, j - i)
                i = j
            else:
                i += 1
        return ans
