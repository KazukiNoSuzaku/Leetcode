# Author: Kaustav Ghosh
# Problem: Lexicographically Smallest String After Applying Operations
# Approach: The reachable state space is tiny, so BFS every string produced by add-to-odd-digits and rotate, tracking the smallest seen

from collections import deque

class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        n = len(s)
        seen = {s}
        queue = deque([s])
        best = s

        while queue:
            cur = queue.popleft()
            if cur < best:
                best = cur

            # Operation 1: add a to every odd-indexed digit (mod 10)
            chars = list(cur)
            for i in range(1, n, 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)

            # Operation 2: rotate right by b
            rotated = cur[-b:] + cur[:-b]

            for nxt in (added, rotated):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)

        return best
