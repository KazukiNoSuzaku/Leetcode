# Author: Kaustav Ghosh
# Problem: Count Artifacts That Can Be Extracted
# Approach: Put every dug cell into a set. An artifact is extractable only when all of the cells in its rectangular footprint have been dug, so count the artifacts whose every covered cell is present in that set

class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        dug = set(map(tuple, dig))
        count = 0
        for r1, c1, r2, c2 in artifacts:
            if all((r, c) in dug
                   for r in range(r1, r2 + 1)
                   for c in range(c1, c2 + 1)):
                count += 1
        return count
