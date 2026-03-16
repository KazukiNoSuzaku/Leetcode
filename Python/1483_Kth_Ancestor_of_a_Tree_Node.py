# Author: Kaustav Ghosh
# Problem: Kth Ancestor of a Tree Node
# Approach: Binary lifting with sparse table

class Solution(object):
    pass

class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        self.LOG = 16
        self.up = [[-1] * n for _ in range(self.LOG)]
        self.up[0] = parent[:]
        for k in range(1, self.LOG):
            for i in range(n):
                if self.up[k - 1][i] != -1:
                    self.up[k][i] = self.up[k - 1][self.up[k - 1][i]]

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        for i in range(self.LOG):
            if k & (1 << i):
                node = self.up[i][node]
                if node == -1:
                    return -1
        return node
