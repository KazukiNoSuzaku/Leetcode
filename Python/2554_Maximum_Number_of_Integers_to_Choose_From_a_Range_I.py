class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        # Greedy: pick smallest non-banned integers from 1..n until sum would exceed maxSum.
        banned_set = set(banned)
        count = total = 0
        for x in range(1, n + 1):
            if x in banned_set:
                continue
            if total + x > maxSum:
                break
            total += x
            count += 1
        return count
