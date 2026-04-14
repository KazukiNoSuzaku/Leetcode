# Author: Kaustav Ghosh
class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        # type: (str, str, List[List[str]]) -> bool
        allowed = {}
        for a, b in mappings:
            if a not in allowed:
                allowed[a] = set()
            allowed[a].add(b)

        n, m = len(s), len(sub)
        for i in range(n - m + 1):
            ok = True
            for j in range(m):
                if s[i + j] == sub[j]:
                    continue
                if sub[j] in allowed and s[i + j] in allowed[sub[j]]:
                    continue
                ok = False
                break
            if ok:
                return True
        return False
