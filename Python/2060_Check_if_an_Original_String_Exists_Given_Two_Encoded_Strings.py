# Author: Kaustav Ghosh
# Problem: Check if an Original String Exists Given Two Encoded Strings
# Approach: DP over (i, j, diff) where diff is how many original characters s1 has consumed beyond s2. A maximal digit run can be split into adjacent numbers many ways, so enumerate all achievable sums. Letters must match when diff is 0, and are absorbed as wildcards when one side is ahead

from functools import lru_cache

class Solution(object):
    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)

        def digit_run_sums(s, i):
            # returns (set of achievable sums, index after the digit run)
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            run = s[i:j]
            sums = set()

            def rec(pos, acc):
                if pos == len(run):
                    sums.add(acc)
                    return
                for e in range(pos + 1, len(run) + 1):
                    if run[pos] != '0':
                        rec(e, acc + int(run[pos:e]))
            rec(0, 0)
            return sums, j

        @lru_cache(maxsize=None)
        def dp(i, j, diff):
            if i == n1 and j == n2:
                return diff == 0
            if diff == 0:
                if i < n1 and s1[i].isdigit():
                    sums, ni = digit_run_sums(s1, i)
                    return any(dp(ni, j, s) for s in sums)
                if j < n2 and s2[j].isdigit():
                    sums, nj = digit_run_sums(s2, j)
                    return any(dp(i, nj, -s) for s in sums)
                if i < n1 and j < n2 and s1[i] == s2[j]:
                    return dp(i + 1, j + 1, 0)
                return False
            if diff > 0:
                # s1 ahead; s2 must consume
                if j == n2:
                    return False
                if s2[j].isdigit():
                    sums, nj = digit_run_sums(s2, j)
                    return any(dp(i, nj, diff - s) for s in sums)
                # letter absorbed as wildcard
                return dp(i, j + 1, diff - 1)
            else:
                # diff < 0: s2 ahead; s1 must consume
                if i == n1:
                    return False
                if s1[i].isdigit():
                    sums, ni = digit_run_sums(s1, i)
                    return any(dp(ni, j, diff + s) for s in sums)
                return dp(i + 1, j, diff + 1)

        return dp(0, 0, 0)
