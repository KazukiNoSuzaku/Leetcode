# Author: Kaustav Ghosh
# Problem: 2246. Longest Path With Different Adjacent Characters
# URL: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
# Difficulty: Hard
#
# Approach:
# DFS on the tree. For each node, collect the longest chain from children
# whose character differs. Keep the top two chains and update the global
# answer with their sum + 1. Return the best single chain + 1 upward.

class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        self.ans = 1
        # Iterative DFS
        stack = [(0, False)]
        longest = [0] * n  # longest chain going down from node i

        while stack:
            node, processed = stack.pop()
            if processed:
                top1 = top2 = 0
                for ch in children[node]:
                    if s[ch] != s[node]:
                        val = longest[ch]
                        if val > top1:
                            top2 = top1
                            top1 = val
                        elif val > top2:
                            top2 = val
                self.ans = max(self.ans, top1 + top2 + 1)
                longest[node] = top1 + 1
            else:
                stack.append((node, True))
                for ch in children[node]:
                    stack.append((ch, False))

        return self.ans
