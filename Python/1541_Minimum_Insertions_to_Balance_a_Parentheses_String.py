# Author: Kaustav Ghosh
# Problem: Minimum Insertions to Balance a Parentheses String
# Approach: Every '(' demands two ')', so carry how many closing brackets are still owed. An opening bracket adds two to the debt, and if the debt was odd a single ')' was left dangling, which costs one insertion to complete. A closing bracket pays one off, and when the debt would go negative a '(' has to be inserted, leaving one ')' still owed. Whatever debt remains at the end is inserted too

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        insertions = 0
        owed = 0
        for ch in s:
            if ch == '(':
                owed += 2
                if owed % 2:
                    insertions += 1
                    owed -= 1
            else:
                owed -= 1
                if owed < 0:
                    insertions += 1
                    owed = 1
        return insertions + owed
