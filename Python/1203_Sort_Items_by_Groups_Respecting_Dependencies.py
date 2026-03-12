# Author: Kaustav Ghosh
# Topological sort at both group and item level

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque

        # Assign unique group ids to ungrouped items
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        # Build group and item graphs
        group_graph = defaultdict(set)
        group_indegree = defaultdict(int)
        item_graph = defaultdict(set)
        item_indegree = defaultdict(int)

        for i in range(n):
            for prev in beforeItems[i]:
                if group[prev] != group[i]:
                    if group[i] not in group_graph[group[prev]]:
                        group_graph[group[prev]].add(group[i])
                        group_indegree[group[i]] += 1
                if prev not in item_graph or i not in item_graph[prev]:
                    item_graph[prev].add(i)
                    item_indegree[i] += 1

        def topo_sort(nodes, graph, indegree):
            queue = deque([n for n in nodes if indegree.get(n, 0) == 0])
            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                for nei in graph.get(node, []):
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            return result if len(result) == len(nodes) else []

        # Get all groups
        all_groups = set(group)
        group_order = topo_sort(all_groups, group_graph, group_indegree)
        if not group_order:
            return []

        # Group items by group
        group_items = defaultdict(list)
        for i in range(n):
            group_items[group[i]].append(i)

        result = []
        for g in group_order:
            items = group_items[g]
            item_order = topo_sort(items, item_graph, item_indegree)
            if len(item_order) != len(items):
                return []
            result.extend(item_order)
        return result
