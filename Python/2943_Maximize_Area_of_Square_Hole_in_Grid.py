from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def longest_consecutive_run(bars: List[int]) -> int:
            bars = sorted(set(bars))
            best = run = 1
            for i in range(1, len(bars)):
                run = run + 1 if bars[i] == bars[i - 1] + 1 else 1
                best = max(best, run)
            return best

        side = min(longest_consecutive_run(hBars), longest_consecutive_run(vBars)) + 1
        return side * side
