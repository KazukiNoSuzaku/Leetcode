class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        last = [0] * 32  # last[b] = rightmost index where bit b is set
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            for b in range(32):
                if nums[i] >> b & 1:
                    last[b] = i
            ans[i] = max(last) - i + 1
        return ans
