from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        def hamming(a, b):
            if len(a) != len(b):
                return float('inf')
            return sum(x != y for x, y in zip(a, b))

        best = 0
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if groups[i] != groups[j] and hamming(words[i], words[j]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[best]:
                best = i

        res, idx = [], best
        while idx != -1:
            res.append(words[idx])
            idx = prev[idx]
        return res[::-1]
