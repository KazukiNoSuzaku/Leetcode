from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        # Sliding window: track equal-pair count; every valid right extension adds (n - r) subarrays.
        freq = defaultdict(int)
        pairs = ans = l = 0
        for r, x in enumerate(nums):
            pairs += freq[x]
            freq[x] += 1
            while pairs >= k:
                freq[nums[l]] -= 1
                pairs -= freq[nums[l]]
                l += 1
            ans += l
        return ans
