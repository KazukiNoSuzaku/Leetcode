from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        score = [1 if x else -1 for x in possible]
        total = sum(score)
        alice = 0
        for i in range(len(score) - 1):
            alice += score[i]
            if alice > total - alice:
                return i + 1
        return -1
