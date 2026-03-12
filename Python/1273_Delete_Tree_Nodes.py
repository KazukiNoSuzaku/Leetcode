# Author: Kaustav Ghosh
# Post-order DFS summing subtrees, prune nodes with sum == 0

class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        from collections import defaultdict
        children = defaultdict(list)
        for i in range(nodes):
            if parent[i] != -1:
                children[parent[i]].append(i)

        def dfs(node):
            total_sum = value[node]
            total_count = 1
            for child in children[node]:
                s, c = dfs(child)
                total_sum += s
                total_count += c
            if total_sum == 0:
                return 0, 0
            return total_sum, total_count

        _, count = dfs(0)
        return count
