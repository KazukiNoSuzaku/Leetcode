import math

class Solution:
    def minOperations(self, k: int) -> int:
        # Start with [1]. Increment costs 1 op, duplicate costs 1 op.
        # Greedy: increment 1 to value v (v-1 ops), then duplicate ceil(k/v)-1 times.
        ans = k - 1
        for v in range(1, k + 1):
            dups = math.ceil(k / v) - 1
            ans = min(ans, (v - 1) + dups)
        return ans
