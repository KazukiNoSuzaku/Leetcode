# Author: Kaustav Ghosh
# Problem: Increasing Decreasing String
# Approach: Repeatedly pick smallest then largest available characters

class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        result = []
        while len(result) < len(s):
            for i in range(26):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1
            for i in range(25, -1, -1):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1
        return ''.join(result)
