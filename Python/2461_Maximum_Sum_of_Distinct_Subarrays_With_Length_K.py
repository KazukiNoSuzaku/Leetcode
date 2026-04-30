from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        window_sum = distinct = ans = 0
        for i, x in enumerate(nums):
            count[x] += 1
            if count[x] == 1:
                distinct += 1
            window_sum += x
            if i >= k:
                left = nums[i - k]
                count[left] -= 1
                if count[left] == 0:
                    distinct -= 1
                window_sum -= left
            if i >= k - 1 and distinct == k:
                ans = max(ans, window_sum)
        return ans
