# Author: Kaustav Ghosh
# Problem: Minimum Insertions to Balance a Parentheses String
# Approach: Each '(' needs '))'; scan tracking unmatched '(' and insert missing ')' or '(' as needed

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        insertions = 0
        open_count = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:
                # consume a pair of ')'; insert one if only a single ')' is present
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    insertions += 1
                    i += 1
                # match against an open '(' or insert one if none is available
                if open_count > 0:
                    open_count -= 1
                else:
                    insertions += 1
        # every remaining unmatched '(' still needs '))'
        insertions += open_count * 2
        return insertions
