# Author: Kaustav Ghosh
# Problem: Shortest Distance to Target String in a Circular Array
# Approach: The array wraps, so reaching index i from the start costs the smaller of walking forward or backward, which is min(d, n - d) for the plain index gap d. Take the smallest such cost over every position holding the target, or -1 when it never appears

class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        best = -1
        for i, word in enumerate(words):
            if word == target:
                gap = abs(i - startIndex)
                steps = min(gap, n - gap)
                best = steps if best == -1 else min(best, steps)
        return best
