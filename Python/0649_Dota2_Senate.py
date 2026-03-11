# Simulate Dota2 senate voting: each senator bans the nearest opponent or wins.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        radiant = deque()
        dire = deque()
        n = len(senate)
        for i, s in enumerate(senate):
            if s == 'R': radiant.append(i)
            else: dire.append(i)
        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()
            if r < d: radiant.append(r + n)
            else: dire.append(d + n)
        return "Radiant" if radiant else "Dire"
