# Author: Kaustav Ghosh
# Problem: Count Number of Texts
# Approach: A maximal run of the same key is decoded independently: a run of length L on a key with m letters (m=4 for '7' and '9', else 3) can be split into consecutive presses of size 1..m, so the count is the number of compositions of L into parts up to m (a tribonacci/tetranacci recurrence). Multiply the counts across runs, modulo 1e9+7

from itertools import groupby


class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(pressedKeys)
        # ways3[i] = compositions of i with parts 1..3; ways4[i] with parts 1..4
        ways3 = [0] * (n + 1)
        ways4 = [0] * (n + 1)
        ways3[0] = ways4[0] = 1
        for i in range(1, n + 1):
            ways3[i] = (ways3[i - 1] + (ways3[i - 2] if i >= 2 else 0) +
                        (ways3[i - 3] if i >= 3 else 0)) % MOD
            ways4[i] = (ways4[i - 1] + (ways4[i - 2] if i >= 2 else 0) +
                        (ways4[i - 3] if i >= 3 else 0) +
                        (ways4[i - 4] if i >= 4 else 0)) % MOD

        result = 1
        for digit, group in groupby(pressedKeys):
            length = len(list(group))
            if digit in '79':
                result = (result * ways4[length]) % MOD
            else:
                result = (result * ways3[length]) % MOD
        return result
