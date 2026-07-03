# Author: Kaustav Ghosh
# Problem: Strange Printer II
# Approach: For each color take its bounding box; any other color inside must be printed later, giving a dependency graph that must be acyclic

class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set(v for row in targetGrid for v in row)

        # Bounding box per color
        box = {}
        for c in colors:
            box[c] = [m, -1, n, -1]  # minr, maxr, minc, maxc
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                b = box[c]
                b[0] = min(b[0], i)
                b[1] = max(b[1], i)
                b[2] = min(b[2], j)
                b[3] = max(b[3], j)

        # graph[c] = colors that must be printed after c (they sit on top inside c's box)
        graph = {c: set() for c in colors}
        for c in colors:
            minr, maxr, minc, maxc = box[c]
            for i in range(minr, maxr + 1):
                for j in range(minc, maxc + 1):
                    if targetGrid[i][j] != c:
                        graph[c].add(targetGrid[i][j])

        state = {c: 0 for c in colors}  # 0 unvisited, 1 visiting, 2 done

        def has_cycle(c):
            state[c] = 1
            for nxt in graph[c]:
                if state[nxt] == 1:
                    return True
                if state[nxt] == 0 and has_cycle(nxt):
                    return True
            state[c] = 2
            return False

        return not any(state[c] == 0 and has_cycle(c) for c in colors)
