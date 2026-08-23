# Author: Kaustav Ghosh
# Problem: Adding Spaces to a String
# Approach: Walk the string; when the current index matches the next requested space position, emit a space before the character. A pointer over the sorted spaces keeps it linear

class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result = []
        p = 0
        m = len(spaces)
        for i, ch in enumerate(s):
            if p < m and i == spaces[p]:
                result.append(' ')
                p += 1
            result.append(ch)
        return ''.join(result)
