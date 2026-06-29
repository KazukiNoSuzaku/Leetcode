# Author: Kaustav Ghosh
# Problem: Find Latest Group of Size M
# Approach: Track each contiguous group's length at its two boundaries; on each set bit merge neighbors and keep a count of groups per length, recording the last step a group of size m exists

class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        n = len(arr)
        length = [0] * (n + 2)   # group length stored at each boundary index
        count = [0] * (n + 1)    # count[L] = number of groups currently of length L
        res = -1
        for step, pos in enumerate(arr):
            left = length[pos - 1]
            right = length[pos + 1]
            new_len = left + right + 1
            length[pos - left] = new_len
            length[pos + right] = new_len
            count[left] -= 1
            count[right] -= 1
            count[new_len] += 1
            if count[m] > 0:
                res = step + 1
        return res
