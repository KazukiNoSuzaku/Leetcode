# Author: Kaustav Ghosh
# Problem: Match Substring After Replacement
# Approach: Build an allowed-replacement map: each character of sub may stay itself or be turned into any of its mapped targets. Slide a window of length len(sub) over s and check every position: the sub character must either equal the s character or list it as an allowed replacement

class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        allowed = {}
        for a, b in mappings:
            allowed.setdefault(a, set()).add(b)

        m, n = len(s), len(sub)
        for start in range(m - n + 1):
            ok = True
            for i in range(n):
                sc = s[start + i]
                pc = sub[i]
                if sc != pc and sc not in allowed.get(pc, ()):
                    ok = False
                    break
            if ok:
                return True
        return False
