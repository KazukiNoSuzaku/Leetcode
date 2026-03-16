# Author: Kaustav Ghosh
# Problem: Frog Position After T Seconds
# Approach: BFS with probability split among children

from collections import defaultdict, deque

class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        if n == 1:
            return 1.0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set([1])
        queue = deque([(1, 1.0)])
        for step in range(t):
            size = len(queue)
            for _ in range(size):
                node, prob = queue.popleft()
                children = [nb for nb in graph[node] if nb not in visited]
                if not children:
                    if node == target:
                        return prob
                    continue
                for child in children:
                    visited.add(child)
                    new_prob = prob / len(children)
                    if step == t - 1 and child == target:
                        return new_prob
                    queue.append((child, new_prob))
            if not queue:
                break

        for node, prob in queue:
            if node == target:
                return prob
        return 0.0
