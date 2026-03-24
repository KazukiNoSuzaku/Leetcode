# Author: Kaustav Ghosh
# Problem 2007: Find Original Array From Doubled Array

from collections import Counter

class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed) % 2 != 0:
            return []
        count = Counter(changed)
        result = []
        for num in sorted(count.keys()):
            if count[num] == 0:
                continue
            if num == 0:
                if count[num] % 2 != 0:
                    return []
                result.extend([0] * (count[num] // 2))
                count[num] = 0
                continue
            if count[num] > count[num * 2]:
                return []
            pairs = count[num]
            result.extend([num] * pairs)
            count[num * 2] -= pairs
            count[num] = 0
        return result
