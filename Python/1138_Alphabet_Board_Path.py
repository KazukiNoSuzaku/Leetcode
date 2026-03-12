# Author: Kaustav Ghosh
# Greedy moves on 5x5+1 alphabet grid, handle 'z' special case by moving up/left first

class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        result = []
        cr, cc = 0, 0
        for ch in target:
            idx = ord(ch) - ord('a')
            tr, tc = idx // 5, idx % 5
            # Move up and left before down and right to avoid going off-grid at 'z'
            if tr < cr:
                result.append('U' * (cr - tr))
            if tc < cc:
                result.append('L' * (cc - tc))
            if tr > cr:
                result.append('D' * (tr - cr))
            if tc > cc:
                result.append('R' * (tc - cc))
            result.append('!')
            cr, cc = tr, tc
        return ''.join(result)
