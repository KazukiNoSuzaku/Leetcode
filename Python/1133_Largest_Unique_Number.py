# Author: Kaustav Ghosh
# Find max element with count == 1

class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(A)
        result = -1
        for num, cnt in count.items():
            if cnt == 1:
                result = max(result, num)
        return result
