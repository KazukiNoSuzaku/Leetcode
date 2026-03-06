# There is a new alien language that uses the English alphabet. However, the order of the
# letters is unknown to you. You are given a list of strings words from the alien language's
# dictionary, where the strings in words are sorted lexicographically by the rules of this language.
# Return a string of the unique letters in the new alien language sorted in ascending order
# as defined by this alien language. If there is no solution return "". If there are multiple
# valid solutions return any of them.

# Example 1:
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

# Constraints:
# 1 <= words.length <= 100

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def alienOrder(self, words):
        adj = defaultdict(set)
        indegree = {c: 0 for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for nb in adj[c]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
        return ''.join(res) if len(res) == len(indegree) else ""
