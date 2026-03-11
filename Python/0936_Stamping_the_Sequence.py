# Find sequence of stamps to produce target string.

# Author: Kaustav Ghosh

class Solution(object):
    def movesToStamp(self, stamp, target):
        m, n = len(stamp), len(target)
        target = list(target)
        res = []
        total = 0
        visited = [False] * (n - m + 1)
        def can_stamp(pos):
            replaced = 0
            for i in range(m):
                if target[pos+i] == '?': continue
                if target[pos+i] != stamp[i]: return 0
                replaced += 1
            return replaced
        def do_stamp(pos):
            for i in range(m): target[pos+i] = '?'
        while total < n:
            stamped = False
            for pos in range(n - m + 1):
                if visited[pos]: continue
                replaced = can_stamp(pos)
                if replaced > 0:
                    do_stamp(pos)
                    total += replaced
                    visited[pos] = True
                    res.append(pos)
                    stamped = True
            if not stamped: return []
        return res[::-1]
