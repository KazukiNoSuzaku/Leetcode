class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n - 1):
            if nums[i + 1] - nums[i] == 1:
                length = 2
                ans = max(ans, length)
                j = i + 2
                while j < n and nums[j] - nums[j - 1] == (1 if (j - i) % 2 == 1 else -1):
                    length += 1
                    ans = max(ans, length)
                    j += 1
        return ans
