# Author: Kaustav Ghosh
# Problem: The Most Similar Path in a Graph
# Approach: The path has the same length as the target, so the only choice at each step is which city to stand in, and the cost of a step is just whether its name differs from the target's. Work backwards: for each step and city, store the cheapest completion, which is that city's mismatch plus the best neighbour's value from the next step. Keeping the chosen neighbour lets the path be read back from the best starting city

class Solution(object):
    def mostSimilar(self, n, roads, names, targetPath):
        """
        :type n: int
        :type roads: List[List[int]]
        :type names: List[str]
        :type targetPath: List[str]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        steps = len(targetPath)
        INF = float('inf')
        cost = [[INF] * n for _ in range(steps)]
        follow = [[-1] * n for _ in range(steps)]
        for city in range(n):
            cost[steps - 1][city] = names[city] != targetPath[steps - 1]

        for i in range(steps - 2, -1, -1):
            ahead = cost[i + 1]
            for city in range(n):
                best = INF
                chosen = -1
                for neighbour in graph[city]:
                    if ahead[neighbour] < best:
                        best = ahead[neighbour]
                        chosen = neighbour
                cost[i][city] = best + (names[city] != targetPath[i])
                follow[i][city] = chosen

        city = min(range(n), key=lambda c: cost[0][c])
        path = [city]
        for i in range(steps - 1):
            city = follow[i][city]
            path.append(city)
        return path
