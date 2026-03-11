# Find minimum turns to reach target from '0000' avoiding deadends.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        dead = set(deadends)
        if '0000' in dead: return -1
        q = deque([('0000', 0)])
        visited = {'0000'}
        while q:
            state, turns = q.popleft()
            if state == target: return turns
            for i in range(4):
                d = int(state[i])
                for delta in [1, -1]:
                    new_d = (d + delta) % 10
                    new_state = state[:i] + str(new_d) + state[i+1:]
                    if new_state not in visited and new_state not in dead:
                        visited.add(new_state)
                        q.append((new_state, turns + 1))
        return -1
