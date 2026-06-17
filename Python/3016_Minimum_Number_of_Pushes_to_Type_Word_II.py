from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Sort frequencies descending; assign highest-freq letters to position 1 (cost 1 each), etc.
        freq = sorted(Counter(word).values(), reverse=True)
        return sum(f * (i // 8 + 1) for i, f in enumerate(freq))
