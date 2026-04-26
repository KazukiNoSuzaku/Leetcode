class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        # dec[i] = length of non-increasing run ending at i
        # inc[i] = length of non-decreasing run starting at i
        dec = [1] * n
        inc = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                dec[i] = dec[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                inc[i] = inc[i + 1] + 1
        return [i for i in range(k, n - k) if dec[i - 1] >= k and inc[i + 1] >= k]
