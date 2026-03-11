# Find minimum number of stickers to spell a target word; return -1 if impossible.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def minStickers(self, stickers, target):
        sticker_counts = [Counter(s) for s in stickers]
        memo = {'': 0}
        def dp(remain):
            if remain in memo: return memo[remain]
            counts = Counter(remain)
            best = float('inf')
            for sc in sticker_counts:
                if sc[remain[0]] == 0: continue
                new_remain = ''
                for c, cnt in counts.items():
                    new_remain += c * max(0, cnt - sc[c])
                sub = dp(new_remain)
                if sub != -1:
                    best = min(best, sub + 1)
            memo[remain] = best if best != float('inf') else -1
            return memo[remain]
        return dp(target)
