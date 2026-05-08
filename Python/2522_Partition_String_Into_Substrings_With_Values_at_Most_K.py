class Solution:
    def minimumPartitionCount(self, s: str, k: int) -> int:
        # Greedy: extend current number while its value stays <= k; otherwise open a new partition.
        ans = 1
        cur = 0
        for c in s:
            d = int(c)
            if d > k:
                return -1
            new_val = cur * 10 + d
            if new_val > k:
                ans += 1
                cur = d
            else:
                cur = new_val
        return ans
