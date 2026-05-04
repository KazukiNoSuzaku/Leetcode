class Solution:
    def maxJump(self, stones: list[int]) -> int:
        # Optimal: alternate stones between two trips.
        # One trip takes even-indexed stones, the other odd-indexed.
        # Max jump = max gap between stones two positions apart.
        ans = stones[1] - stones[0]  # both trips must cover this gap
        for i in range(len(stones) - 2):
            ans = max(ans, stones[i + 2] - stones[i])
        return ans
