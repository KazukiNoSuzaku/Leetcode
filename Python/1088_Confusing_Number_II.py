# Author: Kaustav Ghosh
# 1088. Confusing Number II
# https://leetcode.com/problems/confusing-number-ii/

class Solution(object):
    def confusingNumberII(self, n):
        """
        :type n: int
        :rtype: int
        """
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        valid_digits = [0, 1, 6, 8, 9]
        self.count = 0

        def backtrack(num, rotated, factor):
            if num != rotated and num <= n:
                self.count += 1
            for d in valid_digits:
                if num == 0 and d == 0:
                    continue
                new_num = num * 10 + d
                if new_num > n:
                    break
                new_rotated = mapping[d] * factor + rotated
                backtrack(new_num, new_rotated, factor * 10)

        backtrack(0, 0, 1)
        return self.count
