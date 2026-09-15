# Author: Kaustav Ghosh
# Problem: Find Closest Node to Given Two Nodes
# Approach: Every node has at most one outgoing edge, so the walk from a start node is a single path that either stops or runs into a cycle. Walk from both starts recording each node's distance, then pick the node reached by both with the smallest maximum of the two distances, breaking ties by the smaller index

class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        def walk(start):
            dist = [-1] * len(edges)
            node = start
            step = 0
            while node != -1 and dist[node] == -1:
                dist[node] = step
                step += 1
                node = edges[node]
            return dist

        d1 = walk(node1)
        d2 = walk(node2)
        best = -1
        best_dist = float('inf')
        for i in range(len(edges)):
            if d1[i] != -1 and d2[i] != -1 and max(d1[i], d2[i]) < best_dist:
                best_dist = max(d1[i], d2[i])
                best = i
        return best
