# Author: Kaustav Ghosh
# Problem: Product of Two Run-Length Encoded Arrays
# Approach: Walk both encodings together; each step takes the overlap of the two current runs, emits value1*value2 for that length, and merges with the previous segment when the product repeats

class Solution(object):
    def findRLEArray(self, encoded1, encoded2):
        """
        :type encoded1: List[List[int]]
        :type encoded2: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i = j = 0
        while i < len(encoded1) and j < len(encoded2):
            val = encoded1[i][0] * encoded2[j][0]
            length = min(encoded1[i][1], encoded2[j][1])

            if res and res[-1][0] == val:
                res[-1][1] += length
            else:
                res.append([val, length])

            encoded1[i][1] -= length
            encoded2[j][1] -= length
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        return res
