# Author: Kaustav Ghosh
# 2201. Count Artifacts That Can Be Extracted
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
# Difficulty: Medium
#
# Approach: Build a set of all dug cells, then for each artifact check
# every cell it occupies is in that set.

class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        dug = set()
        for r, c in dig:
            dug.add((r, c))

        count = 0
        for r1, c1, r2, c2 in artifacts:
            can_extract = True
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug:
                        can_extract = False
                        break
                if not can_extract:
                    break
            if can_extract:
                count += 1

        return count
