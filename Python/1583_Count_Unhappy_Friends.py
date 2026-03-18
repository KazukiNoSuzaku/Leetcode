# Author: Kaustav Ghosh
# Problem: 1583 - Count Unhappy Friends
# Approach: Check preference order violations for each pair

class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        # rank[x][y] = rank of y in x's preference list (lower = preferred)
        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for j, person in enumerate(preferences[i]):
                rank[i][person] = j

        paired = {}
        for x, y in pairs:
            paired[x] = y
            paired[y] = x

        unhappy = set()
        for x, y in pairs:
            # x is unhappy if there exists u s.t. x prefers u over y and u prefers x over paired[u]
            for u in preferences[x]:
                if u == y:
                    break
                v = paired[u]
                if rank[u][x] < rank[u][v]:
                    unhappy.add(x)
                    break
            for u in preferences[y]:
                if u == x:
                    break
                v = paired[u]
                if rank[u][y] < rank[u][v]:
                    unhappy.add(y)
                    break

        return len(unhappy)
