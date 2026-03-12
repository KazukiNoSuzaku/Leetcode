# Author: Kaustav Ghosh
# 1087. Brace Expansion
# https://leetcode.com/problems/brace-expansion/

class Solution(object):
    def expand(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        groups = []
        i = 0
        while i < len(s):
            if s[i] == '{':
                j = s.index('}', i)
                groups.append(sorted(s[i+1:j].split(',')))
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1

        result = ['']
        for group in groups:
            result = [prefix + c for prefix in result for c in group]
        return sorted(result)
