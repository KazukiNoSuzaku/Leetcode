from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        beaten = {v for _, v in edges}
        candidates = [i for i in range(n) if i not in beaten]
        return candidates[0] if len(candidates) == 1 else -1
