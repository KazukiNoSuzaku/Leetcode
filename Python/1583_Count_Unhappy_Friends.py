# Author: Kaustav Ghosh
# Problem: Count Unhappy Friends
# Approach: Build a rank table for O(1) preference lookups; x is unhappy if some friend x prefers over its partner also prefers x over theirs

class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        partner = [0] * n
        for a, b in pairs:
            partner[a] = b
            partner[b] = a

        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for idx, f in enumerate(preferences[i]):
                rank[i][f] = idx

        unhappy = 0
        for x in range(n):
            y = partner[x]
            for u in preferences[x]:
                if u == y:
                    break  # remaining friends are all less preferred than x's partner
                v = partner[u]
                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break
        return unhappy
