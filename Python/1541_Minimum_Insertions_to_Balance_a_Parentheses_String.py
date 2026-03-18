# Author: Kaustav Ghosh
# Problem: 1541 - Minimum Insertions to Balance a Parentheses String
# Approach: Track unmatched opens and insertions needed; each '(' needs '))'

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        open_count = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                open_count += 1
                i += 1
            else:
                # need '))'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    result += 1  # insert one ')'
                    i += 1
                if open_count > 0:
                    open_count -= 1
                else:
                    result += 1  # insert one '('
        result += open_count * 2
        return result
