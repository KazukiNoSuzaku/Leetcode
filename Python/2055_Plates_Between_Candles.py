# Author: Kaustav Ghosh
# Problem 2055: Plates Between Candles

from bisect import bisect_left, bisect_right

class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        # Prefix sum of plates
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == '*' else 0)

        # Positions of candles
        candles = [i for i in range(n) if s[i] == '|']

        result = []
        for left, right in queries:
            # Find first candle >= left
            lo = bisect_left(candles, left)
            # Find last candle <= right
            hi = bisect_right(candles, right) - 1
            if lo <= hi:
                l_candle = candles[lo]
                r_candle = candles[hi]
                result.append(prefix[r_candle + 1] - prefix[l_candle])
            else:
                result.append(0)
        return result
