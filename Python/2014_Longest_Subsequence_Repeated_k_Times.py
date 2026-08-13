# Author: Kaustav Ghosh
# Problem: Longest Subsequence Repeated k Times
# Approach: Only letters occurring at least k times can appear. If a candidate repeated k times is a subsequence of s, so is any of its prefixes repeated k times, so valid candidates grow from valid prefixes. BFS by length, extending each valid candidate with allowed letters, and keep the longest (lexicographically largest on ties)

from collections import Counter, deque

class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        freq = Counter(s)
        allowed = [c for c in sorted(set(s)) if freq[c] >= k]

        def is_subseq(t):
            it = iter(s)
            return all(ch in it for ch in t)

        best = ""
        queue = deque([""])
        while queue:
            cur = queue.popleft()
            for c in allowed:
                cand = cur + c
                if is_subseq(cand * k):
                    if len(cand) > len(best) or (len(cand) == len(best) and cand > best):
                        best = cand
                    queue.append(cand)
        return best
