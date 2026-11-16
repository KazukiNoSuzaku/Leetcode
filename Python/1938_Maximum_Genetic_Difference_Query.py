# Author: Kaustav Ghosh
# Problem: Maximum Genetic Difference Query
# Approach: Each query asks for the largest XOR between its value and any node on the path from the root down to its node, which is the classic maximum-XOR-against-a-set problem once that path is available as a set. Answering the queries offline makes every path available for free: a depth-first walk from the root holds exactly the current root-to-node path, so I insert a node's label into a binary trie on entering it, answer every query anchored at that node by walking the trie preferring the branch that disagrees with the query value's bit, and delete the label on leaving. Labels and values both stay under 2^18, the trie keeps a subtree count per edge so deletion is just a decrement, and the walk uses an explicit stack because the tree can be a chain of 10^5 nodes, giving O((n + q) * 18) overall.

class Solution(object):
    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        BITS = 18

        total = len(parents)
        children = [[] for _ in range(total)]
        root = 0
        for node, parent in enumerate(parents):
            if parent == -1:
                root = node
            else:
                children[parent].append(node)

        asked = [[] for _ in range(total)]
        for index, (node, value) in enumerate(queries):
            asked[node].append((value, index))

        branch = [[-1, -1]]
        passing = [0]

        def insert(label):
            at = 0
            for bit in range(BITS - 1, -1, -1):
                side = (label >> bit) & 1
                nxt = branch[at][side]
                if nxt == -1:
                    nxt = len(branch)
                    branch[at][side] = nxt
                    branch.append([-1, -1])
                    passing.append(0)
                at = nxt
                passing[at] += 1

        def remove(label):
            at = 0
            for bit in range(BITS - 1, -1, -1):
                at = branch[at][(label >> bit) & 1]
                passing[at] -= 1

        def best(value):
            at = 0
            score = 0
            for bit in range(BITS - 1, -1, -1):
                wanted = 1 - ((value >> bit) & 1)
                nxt = branch[at][wanted]
                if nxt != -1 and passing[nxt] > 0:
                    score |= 1 << bit
                    at = nxt
                else:
                    at = branch[at][1 - wanted]
            return score

        answers = [0] * len(queries)

        def settle(node):
            for value, index in asked[node]:
                answers[index] = best(value)

        insert(root)
        settle(root)
        stack = [(root, iter(children[root]))]
        while stack:
            node, pending = stack[-1]
            child = next(pending, None)
            if child is None:
                remove(node)
                stack.pop()
            else:
                insert(child)
                settle(child)
                stack.append((child, iter(children[child])))

        return answers
