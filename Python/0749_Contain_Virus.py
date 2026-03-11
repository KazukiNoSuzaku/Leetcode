# Each day, quarantine the most dangerous virus region and spread the rest. Count walls used.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def containVirus(self, isInfected):
        rows, cols = len(isInfected), len(isInfected[0])
        total_walls = 0
        while True:
            visited = [[False]*cols for _ in range(rows)]
            regions = []
            for r in range(rows):
                for c in range(cols):
                    if isInfected[r][c] == 1 and not visited[r][c]:
                        q = deque([(r, c)])
                        visited[r][c] = True
                        cells = [(r, c)]
                        frontiers = set()
                        walls = 0
                        while q:
                            x, y = q.popleft()
                            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                                nx, ny = x+dx, y+dy
                                if 0 <= nx < rows and 0 <= ny < cols:
                                    if isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        cells.append((nx, ny))
                                        q.append((nx, ny))
                                    elif isInfected[nx][ny] == 0:
                                        frontiers.add((nx, ny))
                                        walls += 1
                        regions.append((len(frontiers), walls, cells, frontiers))
            if not regions: break
            regions.sort(reverse=True)
            _, walls, cells, _ = regions[0]
            total_walls += walls
            for r, c in cells: isInfected[r][c] = -1
            for _, _, _, frontiers in regions[1:]:
                for r, c in frontiers: isInfected[r][c] = 1
        return total_walls
