# Author: Kaustav Ghosh
# Problem: Subtree Removal Game with Fibonacci Tree
# Approach: Removing a node with its subtree is Green Hackenbush rooted at the tree root. By the colon principle a branch's nimber is 1 + XOR of its children's branch nimbers, giving B(n) = 1 + (B(n-2) XOR B(n-1)) on the Fibonacci order. Alice wins iff the whole-tree nimber B(n)-1 is nonzero, i.e. B(n) != 1

class Solution(object):
    def findGameWinner(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = [0, 1] + [0] * max(0, n - 1)
        for i in range(2, n + 1):
            b[i] = 1 + (b[i - 2] ^ b[i - 1])
        return b[n] != 1
