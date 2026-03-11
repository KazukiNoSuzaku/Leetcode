# Generate all valid (x, y) coordinate pairs from a string removing one comma.

# Author: Kaustav Ghosh

class Solution(object):
    def ambiguousCoordinates(self, s):
        s = s[1:-1]
        def candidates(part):
            if not part or (len(part) > 1 and part[0] == '0' and part[-1] == '0'): return []
            if len(part) > 1 and part[0] == '0': return ['0.' + part[1:]]
            if part[-1] == '0': return [part]
            res = [part]
            for i in range(1, len(part)):
                res.append(part[:i] + '.' + part[i:])
            return res
        res = []
        for i in range(1, len(s)):
            for x in candidates(s[:i]):
                for y in candidates(s[i:]):
                    res.append('(' + x + ', ' + y + ')')
        return res
