# Author: Kaustav Ghosh
# Problem: 1562 - Find Latest Group of Size M
# Approach: Track group sizes with boundary array, count groups of size M

class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        n = len(arr)
        length = [0] * (n + 2)  # length[i] = length of group containing i
        count = [0] * (n + 2)   # count[k] = number of groups of size k
        result = -1

        for step, pos in enumerate(arr):
            left = length[pos - 1]
            right = length[pos + 1]
            new_len = left + right + 1

            length[pos] = new_len
            length[pos - left] = new_len
            length[pos + right] = new_len

            count[left] -= 1
            count[right] -= 1
            count[new_len] += 1

            if count[m] > 0:
                result = step + 1

        return result
