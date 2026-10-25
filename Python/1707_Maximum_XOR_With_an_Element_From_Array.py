# Author: Kaustav Ghosh
# Problem: Maximum XOR With an Element From Array
# Approach: For a single value, the largest exclusive-or against a set of numbers is found greedily from the top bit down, since setting a higher bit always beats anything the lower bits can offer; a binary trie over the numbers makes that walk possible, taking the opposite branch whenever it exists. The per-query ceiling is handled offline rather than by rebuilding the structure: both the numbers and the queries are sorted, and numbers are inserted as the ceiling rises, so when a query is reached the trie holds exactly the numbers it is permitted to use. An empty trie at that point means no number qualifies, which is the minus one case, and answers are written back by original index so the output order matches the input.

class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        TOP = 29                      # values stay below 2^30
        children = [[-1, -1]]

        def insert(value):
            node = 0
            for bit in range(TOP, -1, -1):
                side = (value >> bit) & 1
                if children[node][side] == -1:
                    children.append([-1, -1])
                    children[node][side] = len(children) - 1
                node = children[node][side]

        def best_against(value):
            node = 0
            result = 0
            for bit in range(TOP, -1, -1):
                side = (value >> bit) & 1
                opposite = 1 - side
                if children[node][opposite] != -1:
                    result |= 1 << bit
                    node = children[node][opposite]
                else:
                    node = children[node][side]
            return result

        ordered = sorted(nums)
        order = sorted(range(len(queries)), key=lambda i: queries[i][1])
        answers = [-1] * len(queries)
        placed = 0
        for index in order:
            value, ceiling = queries[index]
            while placed < len(ordered) and ordered[placed] <= ceiling:
                insert(ordered[placed])
                placed += 1
            if placed:
                answers[index] = best_against(value)
        return answers
