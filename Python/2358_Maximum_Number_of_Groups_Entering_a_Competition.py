import math

class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        # Largest k such that k*(k+1)/2 <= n
        n = len(grades)
        return int((-1 + math.isqrt(1 + 8 * n)) // 2)
