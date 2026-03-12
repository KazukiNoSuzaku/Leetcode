# Author: Kaustav Ghosh
# 1055. Shortest Way to Form String
# https://leetcode.com/problems/shortest-way-to-form-string/

class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        source_set = set(source)
        for c in target:
            if c not in source_set:
                return -1
        count = 0
        j = 0
        n = len(source)
        m = len(target)
        while j < m:
            count += 1
            i = 0
            while i < n and j < m:
                if source[i] == target[j]:
                    j += 1
                i += 1
        return count
