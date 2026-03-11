# Find all words matching a pattern by bijective character mapping.

# Author: Kaustav Ghosh

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def normalize(s):
            mapping = {}
            return tuple(mapping.setdefault(c, len(mapping)) for c in s)
        p = normalize(pattern)
        return [w for w in words if normalize(w) == p]
