class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        base = sum(reward2)
        diffs = sorted((r1 - r2 for r1, r2 in zip(reward1, reward2)), reverse=True)
        return base + sum(diffs[:k])
