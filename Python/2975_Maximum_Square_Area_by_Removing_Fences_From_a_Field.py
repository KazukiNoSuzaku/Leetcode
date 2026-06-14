from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def gaps(fences: List[int], limit: int) -> set:
            pts = sorted([1] + fences + [limit])
            result = set()
            for i in range(len(pts)):
                for j in range(i + 1, len(pts)):
                    result.add(pts[j] - pts[i])
            return result

        hg = gaps(hFences, m)
        vg = gaps(vFences, n)
        common = hg & vg
        return pow(max(common), 2, MOD) if common else -1
