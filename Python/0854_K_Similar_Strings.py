# Find minimum swaps to transform s into t (both are anagrams).

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def kSimilarity(self, s1, s2):
        if s1 == s2: return 0
        q = deque([(s1, 0)])
        visited = {s1}
        while q:
            state, steps = q.popleft()
            i = 0
            while state[i] == s2[i]: i += 1
            for j in range(i + 1, len(state)):
                if state[j] == s2[i]:
                    new = list(state)
                    new[i], new[j] = new[j], new[i]
                    ns = ''.join(new)
                    if ns == s2: return steps + 1
                    if ns not in visited:
                        visited.add(ns)
                        q.append((ns, steps + 1))
        return -1
