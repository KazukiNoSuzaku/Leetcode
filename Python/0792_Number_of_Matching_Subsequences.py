# Count how many words are subsequences of a given string.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, s, words):
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        res = 0
        for c in s:
            for it in waiting.pop(c, []):
                nxt = next(it, None)
                if nxt is None:
                    res += 1
                else:
                    waiting[nxt].append(it)
        return res
