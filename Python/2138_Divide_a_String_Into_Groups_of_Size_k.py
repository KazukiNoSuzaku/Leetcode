# Author: Kaustav Ghosh
# Problem: Divide a String Into Groups of Size k
# Approach: Slice the string into consecutive chunks of length k, padding the final chunk with the fill character if it falls short

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        groups = [s[i:i + k] for i in range(0, len(s), k)]
        if groups and len(groups[-1]) < k:
            groups[-1] += fill * (k - len(groups[-1]))
        return groups
