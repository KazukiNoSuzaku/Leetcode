# Return the minimum number of character replacements to make s an anagram of t.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        diff = Counter(t) - Counter(s)
        return sum(diff.values())
