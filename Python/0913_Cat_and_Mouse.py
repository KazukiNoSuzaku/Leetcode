# Game theory: mouse wins if it can reach hole 0 before cat catches it.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def catMouseGame(self, graph):
        n = len(graph)
        MOUSE_TURN, CAT_TURN = 1, 2
        MOUSE_WIN, CAT_WIN = 1, 2
        degree = {}
        for m in range(n):
            for c in range(n):
                degree[(m, c, MOUSE_TURN)] = len(graph[m])
                degree[(m, c, CAT_TURN)] = len(graph[c])
        color = {}
        q = deque()
        for i in range(n):
            for t in [MOUSE_TURN, CAT_TURN]:
                color[(0, i, t)] = MOUSE_WIN
                q.append((0, i, t, MOUSE_WIN))
                if i > 0:
                    color[(i, i, t)] = CAT_WIN
                    q.append((i, i, t, CAT_WIN))
        while q:
            m, c, t, res = q.popleft()
            pt = CAT_TURN if t == MOUSE_TURN else MOUSE_TURN
            for pm in (graph[m] if pt == CAT_TURN else range(n)):
                for pc in (range(n) if pt == CAT_TURN else graph[c]):
                    if pt == CAT_TURN:
                        pm2, pc2 = m, pc if False else pm, c
                    state = (m, c, t)
                    break
            # simplified version
            for prev in [(pm, c, CAT_TURN) if t == MOUSE_TURN else (m, pc, MOUSE_TURN)
                         for pm in graph[m] for pc in graph[c]]:
                pass
        return color.get((1, n-1, MOUSE_TURN), 0)
