# Given the root of a binary tree, return the most frequent subtree sum.
# The subtree sum is the sum of all the node values formed by the subtree rooted at that node.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def findFrequentTreeSum(self, root):
        count = Counter()
        def subtree_sum(node):
            if not node: return 0
            s = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            count[s] += 1
            return s
        subtree_sum(root)
        max_freq = max(count.values())
        return [k for k, v in count.items() if v == max_freq]
