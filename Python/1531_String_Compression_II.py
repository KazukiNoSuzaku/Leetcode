# Author: Kaustav Ghosh
# Problem: String Compression II
# Approach: Decide the string left to right, remembering only the position and how many deletions are still allowed. At each position either delete the character, or keep it and sweep forward collecting every later copy of it into one run, deleting the differing characters in between; the cost of a run is one character plus the digits of its length when above one. Memoising on (position, deletions left) keeps the search quadratic

from functools import lru_cache


class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        @lru_cache(None)
        def best(i, left):
            if left < 0:
                return float('inf')
            if n - i <= left:
                return 0
            result = best(i + 1, left - 1)
            kept = 0
            deleted = 0
            for j in range(i, n):
                if s[j] == s[i]:
                    kept += 1
                    cost = 1 if kept == 1 else 1 + len(str(kept))
                    result = min(result, cost + best(j + 1, left - deleted))
                else:
                    deleted += 1
                    if deleted > left:
                        break
            return result

        answer = best(0, k)
        best.cache_clear()
        return answer
