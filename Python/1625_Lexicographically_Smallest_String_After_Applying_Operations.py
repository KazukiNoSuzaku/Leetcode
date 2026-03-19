# Author: Kaustav Ghosh
# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        seen = set()
        smallest = s
        queue = [s]
        seen.add(s)
        while queue:
            curr = queue.pop()
            if curr < smallest:
                smallest = curr
            # Add operation
            added = list(curr)
            for i in range(1, len(added), 2):
                added[i] = str((int(added[i]) + a) % 10)
            added = ''.join(added)
            if added not in seen:
                seen.add(added)
                queue.append(added)
            # Rotate operation
            rotated = curr[b:] + curr[:b]
            if rotated not in seen:
                seen.add(rotated)
                queue.append(rotated)
        return smallest
