# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Check mapping consistency and ensure target doesn't use all 26 chars

class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2:
            return True
        mapping = {}
        for c1, c2 in zip(str1, str2):
            if c1 in mapping:
                if mapping[c1] != c2:
                    return False
            else:
                mapping[c1] = c2
        return len(set(str2)) < 26
