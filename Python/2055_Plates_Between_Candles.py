# Author: Kaustav Ghosh
# Problem: Plates Between Candles
# Approach: Precompute a prefix count of plates, the nearest candle at or after each index, and the nearest candle at or before each index. For a query, the innermost candles are the first candle >= left and last candle <= right; the answer is the plate count between them

class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        prefix = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] + (ch == '*')

        left_candle = [-1] * n   # nearest candle at index >= i
        nxt = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                nxt = i
            left_candle[i] = nxt

        right_candle = [-1] * n  # nearest candle at index <= i
        prev = -1
        for i in range(n):
            if s[i] == '|':
                prev = i
            right_candle[i] = prev

        result = []
        for l, r in queries:
            a = left_candle[l]
            b = right_candle[r]
            if a != -1 and b != -1 and a < b:
                result.append(prefix[b] - prefix[a])
            else:
                result.append(0)
        return result
