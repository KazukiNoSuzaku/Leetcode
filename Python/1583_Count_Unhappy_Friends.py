# Author: Kaustav Ghosh
# Problem: Count Unhappy Friends
# Approach: Unhappiness is mutual dissatisfaction between two people in different pairs, so the test for x is whether some u exists whom x ranks above its own partner and who in turn ranks x above their partner. Comparing preferences by scanning the lists would be expensive, so I invert each preference list into a rank table, after which every comparison is a constant-time lookup; then for each x I only need to walk the friends x ranks ahead of its partner, and the first one that reciprocates settles it.

class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        # rank[x][y] is how highly x rates y: smaller means more preferred.
        rank = [[0] * n for _ in range(n)]
        for person, order in enumerate(preferences):
            for position, friend in enumerate(order):
                rank[person][friend] = position

        partner = [0] * n
        for a, b in pairs:
            partner[a] = b
            partner[b] = a

        unhappy = 0
        for x in range(n):
            y = partner[x]
            for u in preferences[x]:
                if u == y:
                    break  # everyone beyond here is rated below x's own partner
                if rank[u][x] < rank[u][partner[u]]:
                    unhappy += 1
                    break
        return unhappy
