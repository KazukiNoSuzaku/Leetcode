# Given a string s, remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"

# Constraints:
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def removeDuplicateLetters(self, s):
        from collections import Counter
        count = Counter(s)
        stack = []
        in_stack = set()
        for c in s:
            count[c] -= 1
            if c in in_stack:
                continue
            while stack and c < stack[-1] and count[stack[-1]] > 0:
                in_stack.remove(stack.pop())
            stack.append(c)
            in_stack.add(c)
        return ''.join(stack)
