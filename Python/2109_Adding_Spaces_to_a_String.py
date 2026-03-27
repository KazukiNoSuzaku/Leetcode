# Author: Kaustav Ghosh
# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result = []
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                result.append(' ')
                j += 1
            result.append(s[i])
        return ''.join(result)
