from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        nums.sort()
        freq = defaultdict(int)
        ans = 0

        def backtrack(idx):
            nonlocal ans
            for i in range(idx, len(nums)):
                if freq[nums[i] - k] == 0:
                    freq[nums[i]] += 1
                    ans += 1
                    backtrack(i + 1)
                    freq[nums[i]] -= 1

        backtrack(0)
        return ans
