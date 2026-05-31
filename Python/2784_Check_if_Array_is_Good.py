from collections import Counter

class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False
        cnt = Counter(nums)
        return cnt[n] == 2 and all(cnt[i] == 1 for i in range(1, n))
