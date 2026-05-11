from bisect import insort, bisect_left

class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        # For each (j,k) with j<k and nums[j]>nums[k]: ans += #{i<j: nums[i]<nums[k]} * #{l>k: nums[l]>nums[j]}.
        n = len(nums)
        ans = 0
        sorted_pre = []
        for j in range(n):
            sfx = [0] * n
            for k in range(n - 2, j, -1):
                sfx[k] = sfx[k + 1] + (nums[k + 1] > nums[j])
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    ans += bisect_left(sorted_pre, nums[k]) * sfx[k]
            insort(sorted_pre, nums[j])
        return ans
