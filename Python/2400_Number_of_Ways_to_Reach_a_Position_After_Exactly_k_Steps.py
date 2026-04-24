from math import comb

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        diff = abs(endPos - startPos)
        # Need `right` steps right and `left` steps left where right-left=diff, right+left=k
        if diff > k or (k - diff) % 2:
            return 0
        right = (k + diff) // 2
        return comb(k, right) % MOD
