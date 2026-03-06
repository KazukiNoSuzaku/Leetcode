# Given a pattern and a string s, return true if s matches the pattern.
# A string matches a pattern if there is a bijective mapping from a letter in pattern to
# a non-empty substring in s.

# Example 1:
# Input: pattern = "aabb", s = "xyzxyzabab"
# Output: false

# Example 2:
# Input: pattern = "aabb", s = "xyzxyzaabb"
# Output: true

# Constraints:
# 1 <= pattern.length, s.length <= 20

# Author: Kaustav Ghosh

class Solution(object):
    def wordPatternMatch(self, pattern, s):
        def backtrack(pi, si, p2w, w2p):
            if pi == len(pattern) and si == len(s):
                return True
            if pi == len(pattern) or si == len(s):
                return False
            p = pattern[pi]
            if p in p2w:
                w = p2w[p]
                if not s[si:].startswith(w):
                    return False
                return backtrack(pi + 1, si + len(w), p2w, w2p)
            for end in range(si + 1, len(s) + 1):
                w = s[si:end]
                if w in w2p:
                    continue
                p2w[p] = w
                w2p[w] = p
                if backtrack(pi + 1, end, p2w, w2p):
                    return True
                del p2w[p]
                del w2p[w]
            return False
        return backtrack(0, 0, {}, {})
