# Author: Kaustav Ghosh
# Problem: Maximum XOR of Two Non-Overlapping Subtrees
# Approach: Number the nodes by an Euler tour: a subtree is the interval between its entry and exit times, and two subtrees are non-overlapping exactly when their intervals are disjoint. Visiting the nodes in order of entry time and feeding a binary trie with every subtree whose exit time already passed keeps the trie holding precisely the legal partners, so one greedy walk down the trie gives the best XOR for each node

class Solution(object):
    def maxXor(self, n, edges, values):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :rtype: int
        """
        BITS = 46
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        entry = [0] * n
        exit_time = [0] * n
        order = []
        parent = [-1] * n
        clock = 0
        stack = [(0, False)]
        seen = [False] * n
        seen[0] = True
        while stack:
            node, leaving = stack.pop()
            if leaving:
                exit_time[node] = clock
                continue
            entry[node] = clock
            clock += 1
            order.append(node)
            stack.append((node, True))
            for nxt in graph[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    parent[nxt] = node
                    stack.append((nxt, False))

        totals = values[:]
        for node in reversed(order):
            if parent[node] != -1:
                totals[parent[node]] += totals[node]

        children = [[-1, -1]]

        def insert(x):
            node = 0
            for bit in range(BITS, -1, -1):
                side = x >> bit & 1
                if children[node][side] == -1:
                    children.append([-1, -1])
                    children[node][side] = len(children) - 1
                node = children[node][side]

        def best_xor(x):
            node = 0
            best = 0
            for bit in range(BITS, -1, -1):
                side = x >> bit & 1
                if children[node][side ^ 1] != -1:
                    best |= 1 << bit
                    node = children[node][side ^ 1]
                else:
                    node = children[node][side]
            return best

        by_entry = sorted(range(n), key=lambda v: entry[v])
        by_exit = sorted(range(n), key=lambda v: exit_time[v])
        answer = 0
        added = 0
        inserted_any = False
        for node in by_entry:
            while added < n and exit_time[by_exit[added]] <= entry[node]:
                insert(totals[by_exit[added]])
                inserted_any = True
                added += 1
            if inserted_any:
                answer = max(answer, best_xor(totals[node]))
        return answer
