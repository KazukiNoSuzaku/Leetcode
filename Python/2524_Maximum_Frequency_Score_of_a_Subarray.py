from collections import Counter

class Solution:
    def maxFrequencyScore(self, nums: list[int], k: int) -> int:
        # Premium: fixed-size sliding window; score = sum(val^freq[val]) mod 10^9+7.
        # On entry freq goes f→f+1: score += val^(f+1) - val^f (or just val when f=0).
        # On exit freq goes f→f-1: score += val^(f-1) - val^f (or -val when f=1).
        MOD = 10**9 + 7
        cnt: Counter = Counter()
        score = 0
        ans = 0
        for r, val in enumerate(nums):
            f = cnt[val]
            score = (score + pow(val, f + 1, MOD) - (pow(val, f, MOD) if f else 0)) % MOD
            cnt[val] += 1
            if r >= k:
                out = nums[r - k]
                fo = cnt[out]
                score = (score - pow(out, fo, MOD) + (pow(out, fo - 1, MOD) if fo > 1 else 0)) % MOD
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
            if r >= k - 1:
                ans = max(ans, score % MOD)
        return ans
