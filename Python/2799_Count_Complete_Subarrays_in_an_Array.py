from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        total = len(set(nums))
        count = defaultdict(int)
        ans = left = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) == total:
                ans += len(nums) - right
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
        return ans
