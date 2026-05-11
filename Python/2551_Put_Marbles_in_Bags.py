class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        # Score = weights[0] + weights[n-1] + sum of chosen split-point pair sums.
        # Difference = sum of top (k-1) adjacent pair sums - sum of bottom (k-1).
        if k == 1:
            return 0
        pairs = sorted(weights[i] + weights[i + 1] for i in range(len(weights) - 1))
        return sum(pairs[-(k - 1):]) - sum(pairs[:k - 1])
