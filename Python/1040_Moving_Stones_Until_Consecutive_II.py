# Author: Kaustav Ghosh
# 1040. Moving Stones Until Consecutive II
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/

class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        n = len(stones)
        # Max moves: move one endpoint at a time
        max_moves = max(stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2)
        # Min moves: sliding window of size n
        min_moves = n
        j = 0
        for i in range(n):
            while j + 1 < n and stones[j+1] - stones[i] < n:
                j += 1
            # stones[i..j] fit in a window of size n
            already = j - i + 1
            if already == n - 1 and stones[j] - stones[i] == n - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - already)
        return [min_moves, max_moves]
