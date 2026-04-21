from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        # good pair: j - i == nums[j] - nums[i]  =>  i - nums[i] == j - nums[j]
        n = len(nums)
        total = n * (n - 1) // 2
        freq = defaultdict(int)
        good = 0
        for i, x in enumerate(nums):
            key = i - x
            good += freq[key]
            freq[key] += 1
        return total - good
