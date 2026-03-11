# You need to construct a binary tree from a string consisting of parenthesis and integers.
# The whole input represents a binary tree. An integer followed by zero, one or two pairs of
# parentheses (left child and right child).

# Author: Kaustav Ghosh

class Solution(object):
    def str2tree(self, s):
        if not s: return None
        idx = [0]
        def parse():
            neg = False
            if idx[0] < len(s) and s[idx[0]] == '-':
                neg = True; idx[0] += 1
            num = 0
            while idx[0] < len(s) and s[idx[0]].isdigit():
                num = num * 10 + int(s[idx[0]]); idx[0] += 1
            node = TreeNode(-num if neg else num)
            if idx[0] < len(s) and s[idx[0]] == '(':
                idx[0] += 1; node.left = parse(); idx[0] += 1  # skip ')'
            if idx[0] < len(s) and s[idx[0]] == '(':
                idx[0] += 1; node.right = parse(); idx[0] += 1
            return node
        return parse()
