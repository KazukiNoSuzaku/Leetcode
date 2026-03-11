# Check if you can escape to target before any ghost reaches it (Manhattan distance).

# Author: Kaustav Ghosh

class Solution(object):
    def escapeGhosts(self, ghosts, target):
        my_dist = abs(target[0]) + abs(target[1])
        return all(abs(g[0]-target[0]) + abs(g[1]-target[1]) > my_dist for g in ghosts)
