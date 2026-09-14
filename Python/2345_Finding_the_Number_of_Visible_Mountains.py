# Author: Kaustav Ghosh
# Problem: Finding the Number of Visible Mountains
# Approach: A peak (x, y) spans the base interval [x - y, x + y], and one mountain hides another exactly when its interval contains the other's. Sort by left end ascending and right end descending so any container comes first; a mountain is visible if its right end beats every earlier right end and it is not identical to the next mountain (duplicates hide each other)

class Solution(object):
    def visibleMountains(self, peaks):
        """
        :type peaks: List[List[int]]
        :rtype: int
        """
        spans = sorted((x - y, -(x + y)) for x, y in peaks)
        count = 0
        max_right = float('-inf')
        for i, (left, neg_right) in enumerate(spans):
            right = -neg_right
            if right > max_right and (i + 1 == len(spans) or spans[i + 1] != spans[i]):
                count += 1
            max_right = max(max_right, right)
        return count
