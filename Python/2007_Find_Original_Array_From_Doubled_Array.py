# Author: Kaustav Ghosh
# Problem: Find Original Array From Doubled Array
# Approach: A doubled array has even length. Sort and greedily match the smallest remaining value x with its double 2x using a count map. Zeros pair with themselves (need an even count). Any unmatched value means no valid original

from collections import Counter

class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed) % 2 == 1:
            return []
        count = Counter(changed)
        result = []
        for x in sorted(changed):
            if count[x] == 0:
                continue
            if x == 0:
                if count[0] < 2:
                    return []
                count[0] -= 2
                result.append(0)
            else:
                if count[2 * x] == 0:
                    return []
                count[x] -= 1
                count[2 * x] -= 1
                result.append(x)
        return result
