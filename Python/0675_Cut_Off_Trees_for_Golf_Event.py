# Find minimum steps to cut all trees in height order; return -1 if impossible.

# Author: Kaustav Ghosh

from collections import deque
import heapq

class Solution(object):
    def cutOffTree(self, forest):
        rows, cols = len(forest), len(forest[0])
        trees = sorted((forest[r][c], r, c) for r in range(rows) for c in range(cols) if forest[r][c] > 1)
        
        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc: return 0
            visited = {(sr, sc)}
            q = deque([(sr, sc, 0)])
            while q:
                r, c, steps = q.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and forest[nr][nc]:
                        if nr == tr and nc == tc: return steps + 1
                        visited.add((nr, nc))
                        q.append((nr, nc, steps + 1))
            return -1
        
        r = c = total = 0
        for _, tr, tc in trees:
            steps = bfs(r, c, tr, tc)
            if steps == -1: return -1
            total += steps
            r, c = tr, tc
        return total
