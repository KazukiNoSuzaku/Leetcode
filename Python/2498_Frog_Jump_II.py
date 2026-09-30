# Author: Kaustav Ghosh
# Problem: Frog Jump II
# Approach: The trip out and the trip back together visit every stone once, so the two routes split the stones into alternating halves. Best case each route skips exactly one stone at a time, making the cost the largest gap between stones two apart, with the single hop from the first stone covering the two-stone case

class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        best = stones[1] - stones[0]
        for i in range(len(stones) - 2):
            best = max(best, stones[i + 2] - stones[i])
        return best
