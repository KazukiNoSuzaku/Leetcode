class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        L = 0
        for a, b, c in zip(s1, s2, s3):
            if a == b == c:
                L += 1
            else:
                break
        if L == 0:
            return -1
        return len(s1) + len(s2) + len(s3) - 3 * L
