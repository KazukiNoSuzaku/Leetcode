# From index i, jump to i+1, i-1, or any j where arr[j]==arr[i].
# Return minimum jumps to reach the last index.

# Author: Kaustav Ghosh

from collections import deque, defaultdict

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        if n == 1: return 0
        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)
        visited = {0}
        q = deque([(0, 0)])
        while q:
            i, steps = q.popleft()
            for j in list(graph[arr[i]]) + [i-1, i+1]:
                if j == n - 1: return steps + 1
                if 0 <= j < n and j not in visited:
                    visited.add(j)
                    q.append((j, steps + 1))
            graph[arr[i]] = []  # clear to avoid revisiting same-value nodes
        return -1
