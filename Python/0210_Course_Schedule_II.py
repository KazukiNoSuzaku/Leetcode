# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
# you must take course bi first if you want to take course ai.
# Return the ordering of courses you should take to finish all courses.
# If there are many valid answers, return any of them. If it is impossible to finish all courses, return [].

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]

# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == numCourses else []
