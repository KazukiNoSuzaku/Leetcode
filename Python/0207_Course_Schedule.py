# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
# you must take course bi first if you want to take course ai.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false

# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# All the pairs prerequisites[i] are unique.

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses
