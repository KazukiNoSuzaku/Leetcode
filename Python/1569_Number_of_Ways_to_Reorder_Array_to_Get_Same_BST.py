# Author: Kaustav Ghosh
# Problem: Number of Ways to Reorder Array to Get Same BST
# Approach: The first element must stay first since it fixes the root, and every later element is forced into the left or right subtree by comparison with it, so the orderings producing the same tree are exactly the interleavings of a valid left-subtree ordering with a valid right-subtree ordering: ways(node) = C(left + right, left) * ways(left) * ways(right). I evaluate that product iteratively over an explicit stack rather than by recursion, because a sorted input would nest a thousand levels deep, and subtract one at the end to exclude the original arrangement.

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)

        # Pascal's triangle up to n rows is enough for every interleaving count.
        choose = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            choose[i][0] = 1
            for j in range(1, i + 1):
                choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % MOD

        result = 1
        stack = [nums]
        while stack:
            group = stack.pop()
            if len(group) <= 2:
                continue
            root = group[0]
            smaller = [v for v in group[1:] if v < root]
            larger = [v for v in group[1:] if v > root]
            result = result * choose[len(smaller) + len(larger)][len(smaller)] % MOD
            stack.append(smaller)
            stack.append(larger)
        return (result - 1) % MOD
