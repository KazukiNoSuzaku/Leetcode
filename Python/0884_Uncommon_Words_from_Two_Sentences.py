# Find words appearing exactly once in one sentence and not in the other.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        count = Counter((s1 + ' ' + s2).split())
        return [w for w, c in count.items() if c == 1]
