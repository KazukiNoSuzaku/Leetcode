# Author: Kaustav Ghosh
# 1036. Escape a Large Maze
# https://leetcode.com/problems/escape-a-large-maze/

from collections import deque

class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        if not blocked:
            return True
        blocked_set = set(map(tuple, blocked))
        limit = len(blocked) * len(blocked) // 2

        def bfs(start, end):
            q = deque([tuple(start)])
            visited = {tuple(start)}
            while q:
                x, y = q.popleft()
                if [x, y] == end:
                    return True
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in blocked_set and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
                if len(visited) > limit:
                    return True
            return False

        return bfs(source, target) and bfs(target, source)
