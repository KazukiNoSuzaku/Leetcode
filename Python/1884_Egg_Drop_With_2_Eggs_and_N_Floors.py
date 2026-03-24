# Author: Kaustav Ghosh
# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

import math

class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        # With k moves and 2 eggs, we can check k*(k+1)/2 floors
        # Find smallest k such that k*(k+1)/2 >= n
        k = int(math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2))
        return k
