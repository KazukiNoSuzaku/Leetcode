# Author: Kaustav Ghosh
# Problem: Course Schedule IV
# Approach: Floyd-Warshall transitive closure

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            reachable[a][b] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        return [reachable[u][v] for u, v in queries]
