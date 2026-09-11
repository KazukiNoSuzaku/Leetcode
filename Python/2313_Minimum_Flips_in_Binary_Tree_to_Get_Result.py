# Author: Kaustav Ghosh
# Problem: Minimum Flips in Binary Tree to Get Result
# Approach: Post-order DP returning, for each node, the minimum leaf flips to make it evaluate False and to make it evaluate True. Leaves cost 0 to keep their value and 1 to flip it. Internal operators (OR/AND/XOR/NOT) combine the children's two costs according to the operator's truth table. The answer reads the root's cost for the requested result

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minimumFlips(self, root, result):
        """
        :type root: Optional[TreeNode]
        :type result: bool
        :rtype: int
        """
        INF = float('inf')

        def solve(node):
            # returns (cost_to_false, cost_to_true)
            if node.left is None and node.right is None:
                if node.val == 0:
                    return (0, 1)
                return (1, 0)
            if node.val == 5:  # NOT
                child = node.left if node.left else node.right
                cf, ct = solve(child)
                return (ct, cf)
            lf, lt = solve(node.left)
            rf, rt = solve(node.right)
            if node.val == 2:  # OR
                cost_true = min(lt + rt, lt + rf, lf + rt)
                cost_false = lf + rf
            elif node.val == 3:  # AND
                cost_true = lt + rt
                cost_false = min(lf + rf, lf + rt, lt + rf)
            else:  # XOR (4)
                cost_true = min(lt + rf, lf + rt)
                cost_false = min(lf + rf, lt + rt)
            return (cost_false, cost_true)

        cf, ct = solve(root)
        return ct if result else cf
