from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                rem = nums[:i] + nums[j + 1:]
                if all(rem[k] < rem[k + 1] for k in range(len(rem) - 1)):
                    ans += 1
        return ans
