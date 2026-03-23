# Author: Kaustav Ghosh
# Problem 1868: Product of Two Run-Length Encoded Arrays (Premium)

class Solution(object):
    def findRLEArray(self, encoded1, encoded2):
        """
        :type encoded1: List[List[int]]
        :type encoded2: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        i = j = 0
        while i < len(encoded1) and j < len(encoded2):
            val = encoded1[i][0] * encoded2[j][0]
            freq = min(encoded1[i][1], encoded2[j][1])
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
            if result and result[-1][0] == val:
                result[-1][1] += freq
            else:
                result.append([val, freq])
        return result
