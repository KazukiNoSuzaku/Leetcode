from collections import defaultdict

class Solution:
    def oddString(self, words: list[str]) -> str:
        groups = defaultdict(list)
        for w in words:
            key = tuple(ord(w[i+1]) - ord(w[i]) for i in range(len(w) - 1))
            groups[key].append(w)
        for ws in groups.values():
            if len(ws) == 1:
                return ws[0]
