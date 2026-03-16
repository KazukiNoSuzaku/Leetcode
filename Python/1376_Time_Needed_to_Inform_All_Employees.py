# Author: Kaustav Ghosh
# Problem: Time Needed to Inform All Employees
# Approach: DFS tree traversal summing inform times

from collections import defaultdict

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        children = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                children[manager[i]].append(i)

        def dfs(node):
            if not children[node]:
                return 0
            return informTime[node] + max(dfs(c) for c in children[node])

        return dfs(headID)
