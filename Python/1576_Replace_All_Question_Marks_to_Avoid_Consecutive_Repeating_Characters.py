# Author: Kaustav Ghosh
# Problem: Replace All ?'s to Avoid Consecutive Repeating Characters
# Approach: For each '?' try 'a'/'b'/'c'; with only two neighbors to avoid, one of these three always fits

class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        n = len(res)
        for i in range(n):
            if res[i] != '?':
                continue
            for ch in 'abc':
                if (i > 0 and res[i - 1] == ch) or (i + 1 < n and res[i + 1] == ch):
                    continue
                res[i] = ch
                break
        return ''.join(res)
