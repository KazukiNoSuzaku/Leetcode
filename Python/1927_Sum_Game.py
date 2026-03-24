# Author: Kaustav Ghosh
# https://leetcode.com/problems/sum-game/

class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        half = n // 2
        left_sum = 0
        left_q = 0
        right_sum = 0
        right_q = 0
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
        # Bob wins (return False) iff left_sum - right_sum + 9 * (left_q - right_q) / 2 == 0
        # and (left_q - right_q) is even
        diff_sum = left_sum - right_sum
        diff_q = left_q - right_q
        # Bob wins when: diff_sum + 9 * diff_q / 2 == 0
        # => 2 * diff_sum + 9 * diff_q == 0
        return 2 * diff_sum + 9 * diff_q != 0
