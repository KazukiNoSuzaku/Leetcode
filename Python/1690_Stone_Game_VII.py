# Author: Kaustav Ghosh
# Problem: Stone Game VII
# Approach: Both players optimise the same quantity, the score difference from the current position onward, so one table suffices rather than one per player: the value of a range is the better of removing either end, where removing an end scores the rest of the range and then concedes whatever the opponent achieves on what remains. Range sums come from a prefix total so each state is constant work. The table is filled by increasing range length, and since a range of a given start only needs the next start's row and its own earlier entries, two rolling rows replace the full square and keep the memory linear.

class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        prefix = [0] * (n + 1)
        for i, value in enumerate(stones):
            prefix[i + 1] = prefix[i] + value

        previous = [0] * n          # best difference for ranges starting at i + 1
        for i in range(n - 2, -1, -1):
            current = [0] * n
            for j in range(i + 1, n):
                total = prefix[j + 1] - prefix[i]
                drop_left = total - stones[i] - previous[j]
                drop_right = total - stones[j] - current[j - 1]
                current[j] = drop_left if drop_left > drop_right else drop_right
            previous = current
        return previous[n - 1]
