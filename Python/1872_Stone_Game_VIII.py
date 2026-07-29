# Author: Kaustav Ghosh
# Problem: Stone Game VIII
# Approach: A move that stops at prefix i scores prefix[i]. Working from the right, the best score difference available from cut i onward is max(defer, prefix[i] - best_from_next); the answer is that value at the first legal cut

class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        best = prefix[n - 1]  # taking all stones
        for i in range(n - 2, 0, -1):
            best = max(best, prefix[i] - best)
        return best
