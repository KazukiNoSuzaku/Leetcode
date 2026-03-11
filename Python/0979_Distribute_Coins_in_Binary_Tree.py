# Each node has some coins; total = number of nodes. In each move, push one coin
# to an adjacent node. Return minimum number of moves needed.

# Author: Kaustav Ghosh

class Solution(object):
    def distributeCoins(self, root):
        self.moves = 0
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.moves += abs(l) + abs(r)
            return node.val + l + r - 1
        dfs(root)
        return self.moves
